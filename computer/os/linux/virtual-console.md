## Virtual Console

A **virtual console** in Linux is a text-based interface that allows multiple independent terminal sessions on the same physical display or machine. Each virtual console operates as if it were a separate terminal, but they're all virtual, meaning they share the same hardware (e.g., keyboard, display) while providing separate environments.

It’s called **virtual** because, unlike a physical terminal, it doesn't have dedicated hardware (like a teletype or dedicated monitor for each session). Instead, the system creates multiple **virtual** instances of a console using software, allowing the user to switch between different terminal sessions while using the same physical hardware.

- **Accessing virtual consoles**: You can switch between them using keyboard shortcuts like `Ctrl + Alt + F1` through `F6` (for different virtual consoles).
- **Purpose**: They allow you to run separate terminal sessions simultaneously. For example, you can run a command in one virtual console, switch to another to run different tasks, and return later.
- **Use case**: Before graphical user interfaces (GUIs) became common, virtual consoles were a way to multitask in a purely text-based environment.

They remain useful today for system administration, troubleshooting, and environments where GUI is not used.
