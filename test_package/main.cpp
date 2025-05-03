#include "hardware/gpio.h"
#include "pico/time.h"

int main(){
    gpio_set_function(7, gpio_function_t::GPIO_FUNC_SIO);
    gpio_set_dir(7, GPIO_OUT);
    while(true){
        gpio_put(7, true);
        sleep_ms(500);
        gpio_put(7, false);
        sleep_ms(500);
    }
}
