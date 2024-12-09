Below are step-by-step instructions for adding syntax highlighting to code blocks within your markdown content and displaying them on your Nuxt Content pages. This setup assumes you’re using Nuxt 3 and Nuxt Content 3.

**Prerequisites:**
- A Nuxt 3 project with Nuxt Content configured.
- Some markdown files in your `content/` directory that contain code blocks (e.g., triple backticks) you want to highlight.

### 1. Configure Highlighting in `nuxt.config.ts`

Nuxt Content provides built-in syntax highlighting via [Shiki](https://shiki.matsu.io/). You can configure highlight settings directly in `nuxt.config.ts`.

Open `nuxt.config.ts` and add a `highlight` section to the `content` options:

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: [
    '@nuxt/content'
  ],
  content: {
    highlight: {
      // Choose a theme, for example 'github-dark' or 'dracula'
      theme: 'github-dark',

      // (Optional) preload languages if you need specific language support
      // preload: ['js', 'ts', 'bash', 'html', 'css']
    }
  }
})
```

**What This Does:**
- The `highlight.theme` option sets the color theme used by Shiki for highlighting code.
- Preloading languages can speed things up if you know which languages your docs contain.

### 2. Add Code Blocks to Your Markdown

In your markdown files within `content/`, ensure that code blocks specify a language for proper highlighting. For example, in `content/introduction.md`:

```md
---
title: "Introduction"
---

# Introduction

Here is a code example in JavaScript:

```js
function greet(name) {
  return `Hello, ${name}!`;
}

console.log(greet('World'));
```
```

By specifying `js` after the triple backticks, Nuxt Content knows to highlight using JavaScript syntax rules.

### 3. Displaying the Content

If you’re already using Nuxt Content to fetch and display your markdown content (e.g., using `queryContent()` and then rendering `doc.body`), the syntax highlighting will happen automatically on any code blocks in your markdown.

A typical Nuxt Content page might look like this (`pages/docs/[slug].vue` as an example):

```vue
<!-- pages/docs/[slug].vue -->
<template>
  <div>
    <h1>{{ doc?.title }}</h1>
    <!-- doc?.body now contains highlighted code blocks if any -->
    <div v-html="doc?.body" />
  </div>
</template>

<script setup>
import { useRoute, useAsyncData } from '#app'
import { queryContent } from '#content'

const route = useRoute()
const slug = route.params.slug

const { data } = await useAsyncData(`doc-${slug}`, () =>
  queryContent(slug).findOne()
)

const doc = data.value
</script>
```

Because Nuxt Content processes markdown to HTML on the server, including code highlighting, by the time `doc.body` is injected into the page, all code blocks are already highlighted.

### 4. Run the Development Server

```bash
npm run dev
```

Visit a page displaying a markdown file with code blocks. You should see highlighted syntax according to the chosen theme.

### 5. Adjusting the Theme or Language Support (Optional)

If you want a different theme, you can choose from the supported Shiki themes:

```ts
highlight: {
  theme: 'dracula' // or 'github-light', 'material-palenight', etc.
}
```

If you need to preload additional languages for better performance or because your docs have rare languages:

```ts
highlight: {
  theme: 'github-dark',
  preload: ['python', 'go', 'rust']
}
```

### 6. Add Custom CSS for Code Blocks (Optional)

If you want to style the code blocks container (e.g., add background, padding, or a border), you can add some global CSS to your project, for example in `app.vue` or a global CSS file:

```css
pre[class*="language-"] {
  padding: 1em;
  border-radius: 0.5em;
  background: #1e1e1e; /* A background matching your theme */
  overflow-x: auto;
}
```

Adjust this styling as needed. The syntax highlighting is primarily handled by the inline styles and classes Shiki injects, but you can still tweak the container’s appearance.

- Nuxt Content integrates with Shiki by default, making syntax highlighting easy.
- Configuring `content.highlight` in `nuxt.config.ts` allows you to choose a theme and languages.
- Code blocks in markdown, when properly annotated with a language identifier, are automatically highlighted.
- The final HTML returned by `doc.body` includes highlighted code ready to display.

With these steps, you can quickly and easily add beautiful syntax highlighting to code examples in your Nuxt Content-powered documentation or blog.
