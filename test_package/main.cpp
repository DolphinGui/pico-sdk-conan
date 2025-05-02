#include "hardware/gpio.h"

int main(){
    gpio_set_function(7, gpio_function_t::GPIO_FUNC_SIO);
    gpio_set_dir(7, true);
    // gpio_set_
}
