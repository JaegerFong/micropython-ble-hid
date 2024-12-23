"""
Copyright © 2024 Walkline Wang (https://walkline.wang)
Gitee: https://gitee.com/walkline/micropython-new-ble-library
"""

"""
Keycode Usage ID:
	https://www.usb.org/sites/default/files/hut1_5.pdf#page=90 @ page 90
"""
REPORT_MAP_DATA = [
    0x05,
    0x01,  # Usage Page (Generic Desktop Ctrls)
    0x09,
    0x06,  # Usage (Keyboard)
    # 控制键
    0xA1,
    0x01,  # Collection (Application)
    0x85,
    0x01,  # 	Report ID (1)
    0x05,
    0x07,  # 	Usage Page (Kbrd/Keypad)
    0x19,
    0xE0,  # 	Usage Minimum (0xE0)
    0x29,
    0xE7,  # 	Usage Maximum (0xE7)
    0x15,
    0x00,  # 	Logical Minimum (0)
    0x25,
    0x01,  # 	Logical Maximum (1)
    0x95,
    0x08,  # 	Report Count (8)
    0x75,
    0x01,  # 	Report Size (1)
    0x81,
    0x02,  # 	Input (Data,Var,Abs)
    # 保留字节
    0x95,
    0x01,  # 	Report Count (1)
    0x75,
    0x08,  # 	Report Size (8)
    0x81,
    0x03,  # 	Input (Const,Var,Abs)
    0x05,
    0x07,  # 	Usage Page (Kbrd/Keypad)
    0x19,
    0x04,  # 	Usage Minimum (0x04)
    0x29,
    0x65,  # 	Usage Maximum (0x65)
    0x15,
    0x00,  # 	Logical Minimum (0)
    0x25,
    0x01,  # 	Logical Maximum (1)
    # 0x95, 0x62,	#	Report Count (98)
    0x95,
    0x68,  # 	Report Count (104)
    0x75,
    0x01,  # 	Report Size (1)
    0x81,
    0x02,  # 	Input (Data,Var,Abs)
    # 0x95, 0x01,	#	Report Count (1)
    # 0x75, 0x06,	#	Report Size (6)
    # 0x81, 0x03,	#	Input (Const,Var,Abs)
    0x05,
    0x08,  # 	Usage Page (LEDs)
    0x95,
    0x05,  # 	Report Count (5)
    0x75,
    0x01,  # 	Report Size (1)
    0x19,
    0x01,  # 	Usage Minimum (Num Lock)
    0x29,
    0x05,  # 	Usage Maximum (Kana)
    0x91,
    0x02,  # 	Output (Data,Var,Abs)
    0x95,
    0x01,  # 	Report Count (1)
    0x75,
    0x03,  # 	Report Size (3)
    0x91,
    0x03,  # 	Output (Const,Var,Abs)
    0xC0,  # End Collection
    0x05,
    0x01,  # USAGE_PAGE (Generic Desktop)
    0x09,
    0x02,  # USAGE (Mouse)
    0xA1,
    0x01,  # COLLECTION (Application)
    0x85,
    0x01,  #   REPORT_ID (1)
    0x09,
    0x01,  #   USAGE (Pointer)
    0xA1,
    0x00,  #   COLLECTION (Physical)
    0x05,
    0x09,  #         Usage Page (Buttons)
    0x19,
    0x01,  #         Usage Minimum (1)
    0x29,
    0x03,  #         Usage Maximum (3)
    0x15,
    0x00,  #         Logical Minimum (0)
    0x25,
    0x01,  #         Logical Maximum (1)
    0x95,
    0x03,  #         Report Count (3)
    0x75,
    0x01,  #         Report Size (1)
    0x81,
    0x02,  #         Input(Data, Variable, Absolute); 3 button bits
    0x95,
    0x01,  #         Report Count(1)
    0x75,
    0x05,  #         Report Size(5)
    0x81,
    0x03,  #         Input(Constant);                 5 bit padding
    0x05,
    0x01,  #         Usage Page (Generic Desktop)
    0x09,
    0x30,  #         Usage (X)
    0x09,
    0x31,  #         Usage (Y)
    0x09,
    0x38,  #         Usage (Wheel)
    0x15,
    0x81,  #         Logical Minimum (-127)
    0x25,
    0x7F,  #         Logical Maximum (127)
    0x75,
    0x08,  #         Report Size (8)
    0x95,
    0x03,  #         Report Count (3)
    0x81,
    0x06,  #         Input(Data, Variable, Relative); 3 position bytes (X,Y,Wheel)
    0xC0,  #   END_COLLECTION
    0xC0,  # END_COLLECTION
]
