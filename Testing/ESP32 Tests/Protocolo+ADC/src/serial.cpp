// #include "serial.h"

// UART_Driver::UART_Driver(int uart_n, int tx_pin, int rx_pin){
//     HardwareSerial serial(uart_n);
//     const int TX = tx_pin;
//     const int RX = rx_pin;
// 	// inicializar el Serial a los pines
//     serial.begin(11500, SERIAL_8N1, RX, TX);
// }

// void loop()
// {
// 	// aqui podríamos usar nuestro puerto serial con normalidad
//     while (serial.available() > 0) {
//         uint8_t byteFromSerial = serial.read();
//         //y lo que sea
//     }
   
//     serial.write(...);
// }
