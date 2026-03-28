# Development Plugin for Avalonia

This repository provides focused skills for building, reviewing, designing, porting, and migrating Avalonia applications with modern XAML/C# patterns on Avalonia **11.3.12**.

## Using Skills in Claude Code

Each skill is available as a Claude Code sub-agent under `.claude/agents/`. Use the `development-plugin-for-avalonia` umbrella agent for broad Avalonia work, or invoke a specialist agent directly when the task scope is clear.

### Umbrella Agent

- `development-plugin-for-avalonia` — routes broad Avalonia work to the right specialist

### Specialist Agents

| Agent | Use for |
|---|---|
| `avalonia-bootstrap-and-lifetime` | Startup, `AppBuilder`, lifetimes, platform bootstrap, AOT build config |
| `avalonia-bindings-and-xaml` | Compiled bindings, `x:DataType`, converters, runtime XAML, AOT-safe markup |
| `avalonia-threading-and-dispatcher` | `Dispatcher.UIThread`, reactive flows, timers, async UI coordination |
| `avalonia-styling-and-resources` | Styles, themes, resources, property system, theme variants, packaging |
| `avalonia-views-and-templating` | View locator, `DataTemplate`, templated parents, tree traversal |
| `avalonia-input-and-commands` | `ICommand`, `KeyBinding`, routed events, focus, gestures, drag/drop |
| `avalonia-controls-and-windowing` | Controls, popups, menus, windows, tray, notifications |
| `avalonia-layout-and-virtualization` | Panels, measure/arrange, custom layout, item virtualization |
| `avalonia-rendering-and-graphics` | Animations, compositor, custom drawing, Skia, OpenGL/Vulkan |
| `avalonia-platform-services` | File pickers, clipboard, launcher, screens, platform integration |
| `avalonia-accessibility-and-validation` | Validation, accessibility semantics, automation properties, focus order |
| `avalonia-testing-diagnostics-and-performance` | Tests, diagnostics, profiling, troubleshooting, performance hardening |
| `avalonia-design-systems` | Design tokens, typography, spacing, shell composition, motion |
| `avalonia-fluent-design` | `FluentTheme`, palette customization, density tuning, Fluent shells |
| `html-css-to-avalonia` | HTML/CSS to Avalonia migration |
| `winforms-to-avalonia` | WinForms to Avalonia migration |
| `wpf-to-avalonia` | WPF to Avalonia migration |
| `winui-to-avalonia` | WinUI/Windows App SDK to Avalonia migration |
| `avalonia-12-migration` | Avalonia 11 → 12 migration planning and execution |

## Shared References

All skills reference documents under `references/`. Key indexes:

- `references/compendium.md` — reference index and task navigation
- `references/00-api-map.md` — curated app-facing API map
- `references/api-index-generated.md` — broad signature lookup (Avalonia 11.3.12)

## Version

Default guidance is pinned to Avalonia `11.3.12`. The `avalonia-12-migration` agent is the only explicit Avalonia 12 lane.
