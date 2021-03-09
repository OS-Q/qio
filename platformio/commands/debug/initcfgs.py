
GDB_DEFAULT_INIT_CONFIG = """
define pio_reset_halt_target
    monitor reset halt
end

define pio_reset_run_target
    monitor reset
end

target extended-remote $DEBUG_PORT
monitor init
$LOAD_CMDS
pio_reset_halt_target
$INIT_BREAK
"""

GDB_STUTIL_INIT_CONFIG = """
define pio_reset_halt_target
    monitor reset
    monitor halt
end

define pio_reset_run_target
    monitor reset
end

target extended-remote $DEBUG_PORT
$LOAD_CMDS
pio_reset_halt_target
$INIT_BREAK
"""

GDB_JLINK_INIT_CONFIG = """
define pio_reset_halt_target
    monitor reset
    monitor halt
end

define pio_reset_run_target
    monitor clrbp
    monitor reset
    monitor go
end

target extended-remote $DEBUG_PORT
monitor clrbp
monitor speed auto
pio_reset_halt_target
$LOAD_CMDS
$INIT_BREAK
"""

GDB_BLACKMAGIC_INIT_CONFIG = """
define pio_reset_halt_target
    set language c
    set *0xE000ED0C = 0x05FA0004
    set $busy = (*0xE000ED0C & 0x4)
    while ($busy)
        set $busy = (*0xE000ED0C & 0x4)
    end
    set language auto
end

define pio_reset_run_target
    pio_reset_halt_target
end

target extended-remote $DEBUG_PORT
monitor swdp_scan
attach 1
set mem inaccessible-by-default off
$LOAD_CMDS
$INIT_BREAK

set language c
set *0xE000ED0C = 0x05FA0004
set $busy = (*0xE000ED0C & 0x4)
while ($busy)
    set $busy = (*0xE000ED0C & 0x4)
end
set language auto
"""

GDB_MSPDEBUG_INIT_CONFIG = """
define pio_reset_halt_target
end

define pio_reset_run_target
end

target extended-remote $DEBUG_PORT
monitor erase
$LOAD_CMDS
pio_reset_halt_target
$INIT_BREAK
"""

GDB_QEMU_INIT_CONFIG = """
define pio_reset_halt_target
    monitor system_reset
end

define pio_reset_run_target
    monitor system_reset
end

target extended-remote $DEBUG_PORT
$LOAD_CMDS
pio_reset_halt_target
$INIT_BREAK
"""

GDB_RENODE_INIT_CONFIG = """
define pio_reset_halt_target
    monitor machine Reset
    $LOAD_CMDS
    monitor start
end

define pio_reset_run_target
    pio_reset_halt_target
end

target extended-remote $DEBUG_PORT
$LOAD_CMDS
$INIT_BREAK
monitor start
"""


TOOL_TO_CONFIG = {
    "jlink": GDB_JLINK_INIT_CONFIG,
    "mspdebug": GDB_MSPDEBUG_INIT_CONFIG,
    "qemu": GDB_QEMU_INIT_CONFIG,
    "blackmagic": GDB_BLACKMAGIC_INIT_CONFIG,
    "renode": GDB_RENODE_INIT_CONFIG,
}


def get_gdb_init_config(debug_options):
    tool = debug_options.get("tool")
    if tool and tool in TOOL_TO_CONFIG:
        return TOOL_TO_CONFIG[tool]
    server_exe = (debug_options.get("server") or {}).get("executable", "").lower()
    if "st-util" in server_exe:
        return GDB_STUTIL_INIT_CONFIG
    return GDB_DEFAULT_INIT_CONFIG
