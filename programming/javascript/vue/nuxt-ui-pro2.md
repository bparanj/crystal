Instructions for Nuxt Content 3, integrating content queries into the Nuxt UI Pro docs template. We’ll query markdown files from the `content` directory, display them as a list of documentation pages in the sidebar, and load the selected page’s content in the main area. We’ll also implement simple next/previous navigation at the bottom of each page.

**Prerequisites:**
- A Nuxt 3 project with Nuxt Content installed and configured.
- Nuxt UI Pro installed and configured for the docs layout.
- Some Markdown documents in your `content` directory.

### 1. Set Up the Content Directory

Create a few markdown files with front matter in `content/`:

```
content/
 ├─ introduction.md
 ├─ getting-started.md
 └─ advanced-features.md
```

Example `introduction.md`:

```md
---
title: "Introduction"
---

# Introduction

Welcome to the introduction page of our docs.
```

Do the same for `getting-started.md` and `advanced-features.md`, ensuring each has a `title` in its front matter. The filenames will serve as slugs.

### 2. Create a Dynamic Page for Docs

We will serve docs at a route like `/docs/[...slug].vue` so any URL under `/docs/` can show a doc. If you prefer a single-level route, use `[slug].vue`.

Create `pages/docs/[slug].vue`:

```vue
<!-- pages/docs/[slug].vue -->
<template>
  <div class="docs-layout">
    <aside class="sidebar">
      <h2>Documentation</h2>
      <ul>
        <li v-for="(page, i) in docsList" :key="page._id">
          <NuxtLink
            :to="`/docs/${page._path}`"
            :class="{'font-bold': page._path === doc?._path}"
          >
            {{ page.title }}
          </NuxtLink>
        </li>
      </ul>
    </aside>

    <main class="content-area">
      <h1>{{ doc?.title }}</h1>
      <div v-html="doc?.body" />

      <div class="flex justify-between mt-8">
        <div v-if="prevDoc">
          <NuxtLink :to="`/docs/${prevDoc._path}`">← {{ prevDoc.title }}</NuxtLink>
        </div>
        <div v-if="nextDoc" class="ml-auto">
          <NuxtLink :to="`/docs/${nextDoc._path}`">{{ nextDoc.title }} →</NuxtLink>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { useRoute, useAsyncData } from '#app'
import { queryContent } from '#content'

const route = useRoute()
const slug = route.params.slug

// Fetch current doc
const { data: currentDoc } = await useAsyncData(`doc-${slug}`, () =>
  queryContent(slug).findOne()
)

// Fetch all docs to build sidebar and find next/previous
const { data: allDocs } = await useAsyncData('docs-list', () =>
  queryContent()
    .only(['title', '_path'])
    .sortBy('title', 'asc')
    .find()
)

const doc = currentDoc.value
const docsList = allDocs.value || []

// Determine next/previous docs
let prevDoc = null
let nextDoc = null

if (doc && docsList.length > 0) {
  const currentIndex = docsList.findIndex(d => d._path === doc._path)
  if (currentIndex > 0) {
    prevDoc = docsList[currentIndex - 1]
  }
  if (currentIndex < docsList.length - 1) {
    nextDoc = docsList[currentIndex + 1]
  }
}

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

.font-bold {
  font-weight: bold;
}
</style>
```

- We query the current doc by its `slug` using `queryContent(slug).findOne()`.
- We also query all docs (`queryContent().only(['title', '_path']).find()`) to build a sidebar and allow next/previous navigation.
- The sidebar loops through `docsList` and highlights the current doc using a bold font.
- Next/previous doc links are determined by finding the current doc’s index in `docsList` and linking to the adjacent entries.
- The `v-html="doc?.body"` displays the doc’s rendered markdown content.

### 3. Create the Docs Layout Using Nuxt UI Pro

We already have a docs-like layout available from Nuxt UI Pro. Modify `layouts/docs.vue` to wrap the page:

```vue
<!-- layouts/docs.vue -->
<template>
  <NLayoutDocs>
    <!-- Top Navigation Bar -->
    <template #header>
      <NLayoutHeader>
        <div class="flex items-center space-x-6">
          <div class="font-bold text-xl">My Docs</div>
          <nav class="flex space-x-4">
            <NuxtLink to="/" class="hover:underline">Home</NuxtLink>
            <NuxtLink to="/about" class="hover:underline">About</NuxtLink>
            <NuxtLink to="/contact" class="hover:underline">Contact</NuxtLink>
          </nav>
        </div>
      </NLayoutHeader>
    </template>

    <!-- The sidebar and content will be part of the page -->
    <!-- We rely on the page template defining .docs-layout structure -->
    <NLayoutMain>
      <NuxtPage />
    </NLayoutMain>
  </NLayoutDocs>
</template>

<script setup>
// No additional script needed
</script>

<style scoped>
/* Additional styling if desired */
</style>
```

**Note:** In the `[slug].vue` page, we defined `.docs-layout`, `.sidebar`, and `.content-area` classes. The Nuxt UI Pro docs layout provides a structural baseline, and we integrate our own classes for flexibility.

### 4. Apply the Layout to Docs Pages

We want our docs pages to use the `docs` layout. In `[slug].vue`:

```vue
<script setup>
definePageMeta({
  layout: 'docs'
})
</script>
```

Add this after the `<script setup>` line in `[slug].vue`.  The doc pages use `docs.vue` layout.

### 5. Create a Redirect from `/docs` to the First Doc

Create `pages/docs/index.vue` to redirect to the first doc (e.g., `introduction`):

```vue
<!-- pages/docs/index.vue -->
<script setup>
import { useRouter } from '#app'

const router = useRouter()
router.push('/docs/introduction')
</script>
```

When users go to `/docs`, they’ll land on the introduction page.

### 6. Run the Dev Server

```bash
npm run dev
```

Open `http://localhost:3000/docs`. It should redirect to `http://localhost:3000/docs/introduction`.

You should see:

- The top navigation bar (Home, About, Contact) from the docs layout.
- The sidebar listing your doc pages (`introduction`, `getting-started`, `advanced-features`), sorted alphabetically.
- The main content area showing the current doc’s title and body.
- At the bottom, next/previous links appear if there are adjacent docs in the list.

Click on a sidebar link to navigate between docs. The main content updates accordingly. Test the next/previous links by navigating to pages in the list.

### 7. Additional Enhancements

- Add more metadata fields (like `order`) to sort docs by a custom order rather than title.
- Add CSS to highlight the active doc in the sidebar.
- Refine the next/previous link styling or add icons.
- Add a search feature using Nuxt Content’s features or additional logic.

- We combined Nuxt Content queries with Nuxt UI Pro’s docs layout to build a docs-like site.
- The sidebar is populated dynamically from the content files, and the main area displays the selected doc.
- Next/previous navigation is implemented by referencing the current doc’s position within the full docs list.
- This approach can be extended and styled further to create a rich, user-friendly documentation site.
