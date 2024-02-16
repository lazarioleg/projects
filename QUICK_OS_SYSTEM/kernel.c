#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
 
/* Check if the compiler thinks you are targeting the wrong operating system. */
#if defined(__linux__)
#error "Incorrect cross-compiler, please use the right target for the OS"
#endif
 
/* This tutorial will only work for the 32-bit ix86 targets. */
#if !defined(__i386__)
#error "This tutorial needs to be compiled with a ix86-elf compiler"
#endif
 
enum vga_color {
    VGA_COLOR_BLACK = 0,
    VGA_COLOR_BLUE = 1,
    VGA_COLOR_GREEN = 2,
    VGA_COLOR_CYAN = 3,
    VGA_COLOR_RED = 4,
    VGA_COLOR_MAGENTA = 5,
    VGA_COLOR_BROWN = 6,
    VGA_COLOR_LIGHT_GREY = 7,
    VGA_COLOR_DARK_GREY = 8,
    VGA_COLOR_LIGHT_BLUE = 9,
    VGA_COLOR_LIGHT_GREEN = 10,
    VGA_COLOR_LIGHT_CYAN = 11,
    VGA_COLOR_LIGHT_RED = 12,
    VGA_COLOR_LIGHT_MAGENTA = 13,
    VGA_COLOR_LIGHT_BROWN = 14,
    VGA_COLOR_WHITE = 15,
};

static const size_t VGA_WIDTH = 80;
static const size_t VGA_HEIGHT = 25;
 
size_t terminal_row;
size_t terminal_column;
uint8_t terminal_color;
uint16_t* terminal_buffer;

static inline uint8_t vga_entry_color(enum vga_color fg, enum vga_color bg) 
{
    return fg | (bg << 4); // Shift background color to the appropriate position
}

static inline uint16_t vga_entry(unsigned char uc, uint8_t color) 
{
    return (uint16_t) uc | (uint16_t) color << 8;
}

// Function to draw a colored pixel at given coordinates
void draw_pixel(int x, int y, uint8_t color) {
    terminal_buffer[y * VGA_WIDTH + x] = vga_entry(' ', color);
}

// Function to draw a line from (x1, y1) to (x2, y2) with given color
void draw_line(int x1, int y1, int x2, int y2, uint8_t color) {
    int x_dis = x2 - x1;
	int y_dis = y2 - y1;

	//neg number flip check
	if (x_dis < 0){
		x_dis = x1 - x2;
	}

	if (y_dis < 0){
		y_dis = y2 - y1;
	}

	//main line function (Bresenham's Line Drawing Algorithm)
	int x_step = x1 < x2 ? 1 : -1;
    int y_step = y1 < y2 ? 1 : -1;
    int error = (x_dis > y_dis ? x_dis : -y_dis) / 2;
    int temp_x, temp_y;

    while (x1 != x2 || y1 != y2) {
        terminal_putentryat(' ', color, x1, y1);

        temp_x = error;
        if (temp_x > -x_dis) {
            error -= y_dis;
            x1 += x_step;
        }
        if (temp_x < y_dis) {
            error += x_dis;
            y1 += y_step;
        }
    }

}

// Function to draw a filled rectangle at (x, y) with given width, height, and color
void draw_filled_rectangle(int x, int y, int width, int height, uint8_t color) {
    for (int i = x; i < x + width; i++) {
        for (int j = y; j < y + height; j++) {
            terminal_putentryat(' ', color, i, j);
        }
    }
}

// Function to draw text at (x, y) with given color
void draw_text(const char* text, int x, int y, uint8_t color) {
    int offset = 0;
    while (*text != '\0') {
        terminal_putentryat(*text, color, x + offset, y);
        text++;
        offset++;
    }
}

size_t strlen(const char* str) 
{
	size_t len = 0;
	while (str[len])
		len++;
	return len;
}
 
void terminal_initialize(void) 
{
	terminal_row = 0;
	terminal_column = 0;
	terminal_color = vga_entry_color(VGA_COLOR_LIGHT_GREY, VGA_COLOR_BLACK);
	terminal_buffer = (uint16_t*) 0xB8000;
	for (size_t y = 0; y < VGA_HEIGHT; y++) {
		for (size_t x = 0; x < VGA_WIDTH; x++) {
			const size_t index = y * VGA_WIDTH + x;
			memmove(terminal_buffer, terminal_buffer + VGA_WIDTH, VGA_WIDTH * (VGA_HEIGHT - 1) * sizeof(uint16_t));
			terminal_buffer[index] = vga_entry(' ', terminal_color);
		}
	}
}
 
void terminal_setcolor(uint8_t color) 
{
	terminal_color = color;
}
 
void terminal_putentryat(char c, uint8_t color, size_t x, size_t y) 
{
	const size_t index = y * VGA_WIDTH + x;
	terminal_buffer[index] = vga_entry(c, color);

	memmove(terminal_buffer, terminal_buffer + VGA_WIDTH, VGA_WIDTH * (VGA_HEIGHT - 1) * sizeof(uint16_t));

	for(size_t x = 0; x < VGA_WIDTH; ++x)
	{
		terminal_buffer[index + x] = vga_entry(' ', terminal_color);
	}
}
 
void terminal_putchar(char c) 
{
	terminal_putentryat(c, terminal_color, terminal_column, terminal_row);
    
    //newline check
	if(c == '\n'){
		terminal_row++;
		terminal_column = 0;
	}

	if (++terminal_column == VGA_WIDTH) {
		terminal_column = 0;
		if (++terminal_row == VGA_HEIGHT)
			terminal_row = 0;
	}
}
 
void terminal_write(const char* data, size_t size) 
{
	for (size_t i = 0; i < size; i++)
		terminal_putchar(data[i]);
}
 
void terminal_writestring(const char* data) 
{
	terminal_write(data, strlen(data));
}
 
extern kernel_main(void) 
{
	terminal_initialize();
	terminal_writestring("Kernel Initalized!\n");
    terminal_writestring("Made by Oleg Lazari EST. 2024");
}