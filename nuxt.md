Below is a step-by-step guide to set up a Nuxt project that uses **Nuxt Content** for managing markdown content and the **Nuxt UI Pro “Docs”** template for styling and layout. The steps assume you have Node.js and npm (or yarn) installed.

---

## 1. Create a New Nuxt Project

```bash
npx nuxi init my-docs
```

- This command scaffolds a basic Nuxt 3 project in the `my-docs` directory.

Then, navigate into the project folder:

```bash
cd my-docs
```

Install dependencies:

```bash
npm install
```
*(Or use `yarn install` if you prefer yarn.)*

---

## 2. Install Nuxt Content

```bash
npm install @nuxt/content
```

In your `nuxt.config.ts` (or `nuxt.config.js`), enable the Content module:
```js
export default defineNuxtConfig({
  modules: [
    '@nuxt/content',
    // other modules...
  ],
  // ...other configs
})
```

Nuxt Content automatically reads markdown files in a `content` folder at the project root.  
Create a `content/` directory if it doesn’t already exist.  

---

## 3. Install Nuxt UI Pro

> **Note:** Nuxt UI Pro is a commercial product. Make sure you have proper access or licensing. If you only have Nuxt UI Free, adapt accordingly.

Install Nuxt UI Pro according to the instructions provided when you purchased it. Typically, it looks like:

```bash
npm install @nuxt/ui-pro
```

Then, enable it in your `nuxt.config.ts`:

```js
export default defineNuxtConfig({
  modules: [
    '@nuxt/content',
    '@nuxt/ui-pro', 
  ],
  // ...
})
```

> **Note:** The exact install command or package name may vary based on the version of Nuxt UI Pro you have. Refer to the official documentation or your product details.

---

## 4. Use the “Docs” Template Layout

Nuxt UI Pro provides premade layout templates, including a “Docs” template.  
In your `app.vue` or a custom layout file (e.g., `layouts/docs.vue`), you can import and apply the template components. For example:

```vue
<template>
  <docs-layout>
    <!-- Your doc pages, navigation, etc. -->
    <nuxt-page />
  </docs-layout>
</template>

<script setup>
import { DocsLayout } from '@nuxt/ui-pro/components'

</script>
```

Depending on the version of Nuxt UI Pro, you might import the layout differently. Follow the official docs for the correct import path and usage.

---

## 5. Add Your Content

With Nuxt Content, you can store markdown files in `content/`. For example:

```
my-docs/
  content/
    index.md
    getting-started.md
    about.md
  pages/
  ...
```

Each markdown file becomes an accessible route. For example, `content/index.md` maps to `/`, and `content/getting-started.md` maps to `/getting-started`.

Inside your markdown files, write your docs:

```md
# Getting Started

Welcome to our docs site! This section will guide you through the basics.

- Step 1
- Step 2
- Step 3
```

---

## 6. Display Markdown Content in the Docs Template

Use the `<ContentDoc>` or `<ContentList>` components (provided by Nuxt Content) within your “Docs” layout or pages. For instance, if you have a dedicated page (e.g., `pages/[...slug].vue` to handle dynamic routes):

```vue
<template>
  <docs-layout>
    <div class="doc-container">
      <content-doc />
    </div>
  </docs-layout>
</template>

<script setup>
import { DocsLayout } from '@nuxt/ui-pro/components'
import { useAsyncData } from '#app'
import { queryContent } from '@nuxt/content'

// If you need to manually fetch data or manipulate content:
const { data } = await useAsyncData('page-content', () =>
  queryContent().where({ /* your filters */ }).find()
)
</script>
```

Typically, you might use Nuxt Content’s built-in route mapping. But if you want custom routes or advanced logic, you can manually fetch content with `queryContent()`.

---

## 7. Customize Styling and Navigation

- **Styling:** Nuxt UI Pro often includes utility classes and components. Override or extend them in your global CSS or config.  
- **Navigation:** Docs layouts usually come with a sidebar or top nav. Configure them in a config file or directly in the layout. For instance, create a `navigation.json` or JS object that defines sections and links.

---

## 8. Run the Development Server

Finally, start the dev server:

```bash
npm run dev
```

Open your browser at [http://localhost:3000](http://localhost:3000) to see your docs site in action.

---

## Key Takeaways

1. **Set up Nuxt 3**: Initialize a fresh project.  
2. **Install Nuxt Content**: Manage markdown-based content easily.  
3. **Add Nuxt UI Pro**: Use the pro docs layout and components.  
4. **Structure Your Docs**: Place `.md` files in `content/`.  
5. **Use Provided Layouts**: Import and wrap your pages in the “Docs” layout.  
6. **Configure Navigation**: Customize the sidebar or header to match your site.  

By combining Nuxt Content’s dynamic markdown handling with the Docs layout from Nuxt UI Pro, you get a professional-looking documentation site without building everything from scratch.