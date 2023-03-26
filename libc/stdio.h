#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include "tty.h"
#if !defined(__i386__)
#error "Enjoy your debugging :)"
#endif
 


void write_to(char c, uint8_t color, size_t x, size_t y) 
{
	const size_t index = y * VGA_WIDTH + x;
	terminal_buffer[index] = vga_entry(c, color);
}
 
void putchar(char c) 
{
    
	write_to(c, terminal_color, terminal_column, terminal_row);
	if (++terminal_column == VGA_WIDTH) {
		terminal_column = 0;
		if (++terminal_row == VGA_HEIGHT)
			terminal_row = 0;
	}
}
 
void write(const char* data, size_t size) 
{
	int n;
	for (size_t i = 0; i < size; i++) {
        while (data[i]=='\n') {
            terminal_row = terminal_row + 1;
            terminal_column = 0;
            i++;
        }
        
		putchar(data[i]);
		n=i;
    }
}
 
void printf(const char* data) 
{
	write(data, strlen(data));
}