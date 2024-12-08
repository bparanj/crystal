Below are revised instructions using Nuxt Content (version compatible with Nuxt 3), which provides the `queryContent()` composable for querying Markdown files. We’ll create a basic documentation structure with a sidebar listing all available pages and a main content area that displays the selected doc. This approach mimics a typical docs layout, showing how to integrate a navigation sidebar with Nuxt Content 3.

**Prerequisites:**
- A Nuxt 3 project set up.
- Nuxt Content installed:  
  ```bash
  npm install @nuxt/content
  ```
- Add `@nuxt/content` to `modules` in your `nuxt.config.ts`:
  ```ts
  // nuxt.config.ts
  export default defineNuxtConfig({
    modules: [
      '@nuxt/content'
    ]
  })
  ```

**Note:** Nuxt Content 3 introduces `queryContent()` and no longer uses `$content`.

---

### Step-by-Step Instructions

#### 1. Create `content` Directory and Add Markdown Files

Create a `content` directory at the root of your Nuxt project if it doesn’t exist:

```
my-nuxt-app/
 ├─ content/
 ├─ pages/
 ├─ ...
```

Add a few Markdown files to `content/`, each with a title in its front matter:

- `content/introduction.md`:
  ```md
  ---
  title: "Introduction"
  ---

  # Introduction
  Welcome to the docs! This is the introduction page.
  ```

- `content/getting-started.md`:
  ```md
  ---
  title: "Getting Started"
  ---

  # Getting Started
  Here are the steps to get started...
  ```

- `content/advanced-features.md`:
  ```md
  ---
  title: "Advanced Features"
  ---

  # Advanced Features
  Explore advanced options here...
  ```

#### 2. Create a Dynamic Page to Display Docs

We want all docs under `/docs/`. Let’s create `pages/docs/[slug].vue`. This page will:

- Fetch the requested doc based on the `slug`.
- Fetch a list of all docs to show in a sidebar.
- Display the current doc’s title and content in the main area.

```vue
<!-- pages/docs/[slug].vue -->
<template>
  <div class="docs-layout">
    <aside class="sidebar">
      <h2>Documentation</h2>
      <ul>
        <li v-for="docItem in docsList" :key="docItem._id">
          <NuxtLink :to="`/docs/${docItem._path}`">{{ docItem.title }}</NuxtLink>
        </li>
      </ul>
    </aside>
    <main class="content-area">
      <h1>{{ doc?.title }}</h1>
      <div v-html="doc?.body" />
    </main>
  </div>
</template>

<script setup>
import { useRoute, useAsyncData } from '#app'
import { queryContent } from '#content'

const route = useRoute()
const slug = route.params.slug

// Fetch the current doc
const { data: currentDoc } = await useAsyncData(`doc-${slug}`, () =>
  queryContent(slug).findOne()
)

// Fetch a list of all docs for the sidebar
const { data: docList } = await useAsyncData('docs-list', () =>
  queryContent().only(['title', '_path']).sortBy('title', 'asc').find()
)

const doc = currentDoc.value
const docsList = docList.value || []
</script>

<style scoped>
.docs-layout {
  display: flex;
  gap: 20px;
}

.sidebar {
  width: 200px;
  border-right: 1px solid #ccc;
  padding-right: 10px;
}

.content-area {
  flex: 1;
}
</style>
```

**What Changed from Nuxt Content 2 to Nuxt Content 3:**
- We now use `queryContent()` from `#content` instead of `$content`.
- Document properties like `_path` and `_id` are standard fields returned by `queryContent()`.
- The rest of the logic remains similar, but now we rely on modern Nuxt 3 composables.

#### 3. Create a Default Page or Redirect for `/docs`

When users go to `/docs`, we can redirect them to `introduction.md`. Create `pages/docs/index.vue`:

```vue
<!-- pages/docs/index.vue -->
<script setup>
import { useRouter } from '#app'

const router = useRouter()
router.push('/docs/introduction')
</script>
```

This ensures `/docs` goes straight to the introduction page.

#### 4. Run the Development Server

```bash
npm run dev
```

Open `http://localhost:3000/docs`. You should be redirected to `http://localhost:3000/docs/introduction`, and see the introduction page’s content displayed. The sidebar lists all your markdown docs by title.

Click around the links in the sidebar to navigate between docs. The URL and the displayed doc update accordingly.

#### 5. Optional Enhancements

- Add frontmatter fields like `order` to control the sorting of docs, then adjust `.sortBy()` accordingly.
- Style the sidebar to highlight the active doc.
- Add error handling if a doc is not found.
- Add a layout file (e.g., `layouts/docs.vue`) if you want a more complex structure and apply it to the docs pages with `definePageMeta({ layout: 'docs' })`.

---

**Key Takeaways:**

- Using `queryContent()` in Nuxt Content 3 lets you query markdown documents easily.
- Dynamic routes (`[slug].vue`) make it simple to serve any doc file based on its filename.
- Displaying a list of docs in a sidebar and showing their content in the main area provides a docs-like structure.
- Nuxt 3’s composables (`useAsyncData`, `useRoute`) and file-based routing simplify building a documentation system with navigation and content retrieval.
