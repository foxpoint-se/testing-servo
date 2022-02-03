# usage: python gpio_udev_setup.py --user <username>
# eg: python gpio_udev_setup.py --user ubuntu
# sets up udev rule for gpio devices to be owned
# by gpio group, and user provided
import grp
import subprocess
import argparse


def ensure_gpio_access(gpiouser, gpiogroup):
    try:
        grp.getgrnam(gpiogroup)
        print("group `gpio` already exists")
    except KeyError:
        print("creating {} system group".format(gpiogroup))
        subprocess.call(["groupadd", "-f", "-r", "gpio"])
        gpio_udev_rules()

    subprocess.call(["adduser", gpiouser, gpiogroup])


def gpio_udev_rules():
    with open("/etc/udev/rules.d/99-gpio.rules", "w") as f:
        f.write(
            """SUBSYSTEM=="bcm2835-gpiomem", KERNEL=="gpiomem", GROUP="gpio", MODE="0660"
SUBSYSTEM=="gpio",  GROUP="gpio", MODE="0660"
"""
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Setup udev rules for gpio devices")
    parser.add_argument(
        "--user", type=str, help="specify user that will gain gpio group access"
    )
    args = parser.parse_args()
    group = "gpio"
    user = args.user
    print("user: {}, group: {}\n".format(user, group))
    ensure_gpio_access(user, group)
