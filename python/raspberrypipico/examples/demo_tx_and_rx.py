'''
  # demo_tx_and_rx.py
  #
  # Demo updated for Raspberry Pi Pico running Circuitpython.
  # @author Kevin (@diyelectromusic)
  # Based on original demo_tx_and_rx.py for the Raspberry Pi, details below.
  #
  # brief Receive and transmit data via UART. Read the data sent by TX pin via pin RX.
  # Experiment phenomenon: connect the TX to RX in Sub UART1 and UART2. Read the data sent by Sub UART and print it out.
  #
  # @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  # @licence     The MIT License (MIT)
  # @author [Arya](xue.peng@dfrobot.com)
  # @version  V1.0
  # @date  2021-05-17
  # @get from https://www.dfrobot.com
  # @url https://github.com/DFRobot/DFRobot_IICSerial
'''

import board
import sys
import os
import time

i2c = board.I2C()

from DFRobot_IIC_Serial_Pico import *

iic_uart1 = DFRobot_IIC_Serial(i2c, sub_uart_channel = SUBUART_CHANNEL_1, IA1 = 1, IA0 = 1) #using UART1 interface of IIC to dual uart moudle.
iic_uart2 = DFRobot_IIC_Serial(i2c, sub_uart_channel = SUBUART_CHANNEL_2, IA1 = 1, IA0 = 1) #using UART2 interface of IIC to dual uart moudle.


if __name__ == "__main__":
  iic_uart1.begin(baud = 115200, format = IIC_Serial_8N1)
  iic_uart2.begin(baud = 115200, format = IIC_Serial_8N1)

  print("\n+--------------------------------------------+")
  print("|  Connected UART1's TX pin to RX pin.       |")   #Connect pin TX and RX of UART1 
  print("|  Connected UART2's TX pin to RX pin.       |")   #Connect pin TX and RX of UART2
  print("|  UART1 send a String: \"hello, Serial2!\"    |") #UART1 transmit a string "hello, Serial1!"
  print("|  UART2 send a number: 123                  |")   #UART2 transmit numbers 123
  print("+--------------------------------------------+")
  iic_uart1.printf("hello, Serial2!") #UART1 transmit string:"hello, Serial1!"
  iic_uart2.write('123') #UART2 transmit:123
  print("Serial to print UART1 and UART2's receive data.")
  flag = 0
  while True:
    if iic_uart1.available():
      flag = 0
      while iic_uart1.available():
        if flag == 0:
          print("\nUART1 receive data: ",end='')
          flag = 1
        c = iic_uart1.read(1)
        print(c, end='')
    if iic_uart2.available():
      flag = 0
      while iic_uart2.available():
        if flag == 0:
          print("\nUART2 receive data: ",end='')
          flag = 1
        c = iic_uart2.read(1)
        print(c, end='')
    time.sleep(1)
