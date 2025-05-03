#include "hardware/gpio.h"
#include "pico/time.h"
#include "pico/stdio.h"
#include <cstdio>

int main(){
    gpio_set_function(7, gpio_function_t::GPIO_FUNC_SIO);
    gpio_set_dir(7, GPIO_OUT);
    stdio_init_all();
    while(true){
        gpio_put(7, true);
        printf("On!\n");
        sleep_ms(500);
        gpio_put(7, false);
        printf("Off!\n");
        sleep_ms(500);
    }
}
