# Development Plugin for Avalonia

This repository provides focused skills for building, reviewing, designing, porting, and migrating Avalonia applications with modern XAML/C# patterns on Avalonia **11.3.12**.

## Using Skills in Claude Code

Each skill is available as a Claude Code sub-agent under `.claude/agents/`. Claude Code automatically discovers these agents and can delegate tasks to them.

**How agent invocation works in Claude Code:**
- For broad Avalonia questions, just ask normally — the `development-plugin-for-avalonia` umbrella agent routes to the right specialist.
- To target a specialist directly, mention the area explicitly in your prompt (e.g., "using Avalonia bindings…", "help me migrate from WPF…").
- Claude Code selects and runs the appropriate sub-agent automatically based on your description.

### Quickstart

Here are some typical prompts that trigger the plugin and delegate to the right specialist agent:

```
# Broad / project-level questions — handled by the umbrella agent
"Help me build an Avalonia MVVM app with a sidebar and a details panel."
"Review my Avalonia project structure and suggest improvements."

# Startup and bootstrapping
"Set up an Avalonia app with a custom AppBuilder for a Linux desktop target."
"How do I configure AOT publishing for an Avalonia app on macOS?"

# Bindings and XAML
"Add a compiled binding from my ViewModel's IsLoading property to a spinner visibility."
"Why is my x:DataType binding not resolving at compile time?"

# Threading and async
"I'm calling an API and want to update the UI — show me the correct Dispatcher.UIThread pattern."
"How do I use ObservableAsPropertyHelper from ReactiveUI in an Avalonia ViewModel?"

# Styling and theming
"Create a reusable ControlTheme for a rounded button with a hover state."
"How do I switch between light and dark FluentTheme at runtime?"

# Views and templates
"Wire up a ViewLocator so each ViewModel maps to its View automatically."
"Show me a DataTemplate for a heterogeneous list where items have different types."

# Input and commands
"Add a keyboard shortcut (Ctrl+S) that invokes a SaveCommand on my ViewModel."
"How do I implement drag-and-drop reordering in a ListBox?"

# Controls and windowing
"Open a child window as a dialog and await its result before continuing."
"Add a system-tray icon with a context menu to my Avalonia desktop app."

# Layout and virtualization
"Build a responsive two-column layout that stacks vertically on narrow windows."
"My VirtualizingStackPanel is slow with 50,000 items — help me profile and fix it."

# Rendering and graphics
"Animate a panel sliding in from the right when it becomes visible."
"Draw a custom chart using DrawingContext inside an Avalonia control."

# Platform services
"Show me how to open a file picker and read the selected file path."
"Copy rich text to the clipboard and paste plain text on demand."

# Accessibility and validation
"Add INotifyDataErrorInfo validation to my login form with inline error messages."
"Set AutomationProperties on my custom button so screen readers announce it correctly."

# Testing and diagnostics
"Write a headless unit test for my ViewModel's command guard logic."
"My Avalonia app leaks memory after navigating between views — help me diagnose it."

# Design systems
"Define a spacing and typography scale as resource tokens for a professional B2B app."
"Build a dense data-grid layout suitable for a financial dashboard."

# Fluent design
"Customize the FluentTheme accent color and adjust control corner radii globally."
"Create a Fluent-style navigation shell with a collapsible side rail."

# Migration from other frameworks
"Migrate this WPF UserControl with a DependencyProperty to Avalonia."
"Port my WinForms DataGridView to an Avalonia DataGrid with sorting."
"Convert this WinUI NavigationView shell to Avalonia's equivalent."
"Translate this HTML/CSS card component to an Avalonia ControlTemplate."
"Plan the upgrade of my Avalonia 11 app to Avalonia 12."
```

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
