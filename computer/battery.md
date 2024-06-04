upower -i /org/freedesktop/UPower/devices/battery_BAT0
upower -i `upower -e | grep 'BAT'`
upower -i $(upower -e | grep BAT) | grep --color=never -E "state|to\ full|to\ empty|percentage"

cat /sys/class/power_supply/BAT0/capacity
find /sys/class/power_supply/BAT0/ -type f | xargs -tn1 cat




