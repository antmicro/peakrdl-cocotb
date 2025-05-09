from munch import Munch

reg_map = Munch.fromDict({
    "base_addr": 0,
    "start_addr": 0,
    "CTRL": {
        "base_addr": 0,
        "offset": 0,
        "PRESCALER": {
            "low": 0,
            "mask": 3,
            "reset": 0,
            "sw": "rw",
            "hw": "r",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        },
        "MODE": {
            "low": 2,
            "mask": 12,
            "reset": 0,
            "sw": "rw",
            "hw": "r",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        },
        "MASTER": {
            "low": 4,
            "mask": 16,
            "reset": 0,
            "sw": "rw",
            "hw": "rw",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        },
        "DORD": {
            "low": 5,
            "mask": 32,
            "reset": 0,
            "sw": "rw",
            "hw": "r",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        },
        "ENABLE": {
            "low": 6,
            "mask": 64,
            "reset": 0,
            "sw": "rw",
            "hw": "r",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        },
        "CLK2X": {
            "low": 7,
            "mask": 128,
            "reset": 0,
            "sw": "rw",
            "hw": "r",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        }
    },
    "INTCTRL": {
        "base_addr": 1,
        "offset": 1,
        "INTLVL": {
            "low": 0,
            "mask": 3,
            "reset": 0,
            "sw": "rw",
            "hw": "r",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        }
    },
    "STATUS": {
        "base_addr": 2,
        "offset": 2,
        "WRCOL": {
            "low": 6,
            "mask": 64,
            "reset": 0,
            "sw": "r",
            "hw": "rw",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        },
        "IF": {
            "low": 7,
            "mask": 128,
            "reset": 0,
            "sw": "r",
            "hw": "rw",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        }
    },
    "DATA": {
        "base_addr": 3,
        "offset": 3,
        "WDATA": {
            "low": 0,
            "mask": 255,
            "sw": "w",
            "hw": "r",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        },
        "RDATA": {
            "low": 0,
            "mask": 255,
            "sw": "r",
            "hw": "w",
            "woclr": 0,
            "rclr": 0,
            "hwclr": 0
        }
    }
})
