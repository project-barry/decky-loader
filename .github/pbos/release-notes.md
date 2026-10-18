Decky Loader @TAG@, built natively for ARM64 Linux for PB-OS devices.

- Built from upstream [@TAG@](https://github.com/SteamDeckHomebrew/decky-loader/releases/tag/@TAG@) source (commit @SHA@); no code changes.
- Built on Ubuntu 24.04 (glibc 2.39), so it runs on SteamOS for ARM; upstream's own `PluginLoader-arm64` targets a newer glibc.
- Built by [pbos-upstream-release.yml](https://github.com/project-barry/decky-loader/blob/pbos-arm64/.github/workflows/pbos-upstream-release.yml) ([run](@RUN@)); checked: aarch64, version @TAG@, glibc @GLIBC@ or older.
- Only `PluginLoader-arm64` is here. For x86_64 and other platforms, use [upstream's releases](https://github.com/SteamDeckHomebrew/decky-loader/releases).

The build change was made with Claude Code (Claude Opus 5.5); see the fork's README note.

Decky Loader is licensed under GPL-2.0 (see [LICENSE](https://github.com/project-barry/decky-loader/blob/pbos-arm64/LICENSE)). All credit for Decky Loader goes to the SteamDeckHomebrew team.
