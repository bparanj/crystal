In Vue 3, the terms "composable" and "component" refer to different concepts, each serving a unique purpose in building Vue applications:

1. **Components**:
   - **Definition**: Components are reusable Vue instances with a name. They encapsulate Vue features and markup that can be used in multiple places in your application. A component in Vue can include template, script, and style sections.
   - **Usage**: You use components to build the UI of your application. They can be as simple as a button or as complex as a complete form.
   - **Characteristics**: Components can have their own state, lifecycle hooks, and can emit events. They are the building blocks of a Vue application, used to create a tree-like structure of the UI.

2. **Composables**:
   - **Definition**: Composables are a concept introduced in Vue 3 as part of the Composition API. A composable is a reusable function that encapsulates and manages a piece of reactive state or behavior. 
   - **Usage**: Composables are used to extract and reuse logic across different components. This could include data fetching, form handling, or any other reactive logic.
   - **Characteristics**: Composables make it easier to organize and share logic between components without needing to rely on the options API (like mixins or higher-order components). They leverage Vue’s reactivity system, typically returning reactive state or functions that manipulate that state.

## Key Differences

- **Purpose and Scope**: Components are used for building the UI and structuring the application layout, while composables are used for extracting and managing reactive logic and state.
- **Reusability**: While both are reusable, components are more about reusing template structure and UI elements, whereas composables focus on reusing JavaScript logic and state management.
- **API and Structure**: Components follow Vue's options API or the Composition API structure with a template, script, and style. Composables are purely JavaScript functions, utilizing the Composition API's reactivity features.

In Vue 3, while components are the backbone for your application's UI, composables provide a powerful way to abstract and reuse reactive logic across those components.