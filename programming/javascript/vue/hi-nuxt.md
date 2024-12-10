Instructions to create a basic Nuxt 3 application using the Nuxt Content module. We’ll add Markdown files to the `content` directory, then fetch and display their data within a page. 

**Steps:**

### 1. Create a New Nuxt 3 Project

Run the Nuxt CLI command:

```bash
npx nuxi init nuxt-content-app
```
This creates a `nuxt-content-app` directory with a standard Nuxt 3 setup.

Move into the project directory:
```bash
cd nuxt-content-app
```

Install dependencies:
```bash
npm install
```

### 2. Install the Nuxt Content Module

```bash
npm install @nuxt/content
```

Open `nuxt.config.ts` and add the `@nuxt/content` module to the `modules` array:
```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: [
    '@nuxt/content'
  ]
})
```

This integrates Nuxt Content into your application.

### 3. Create the Content Directory and Add Markdown Files

Create a `content` directory at the project root:

```
nuxt-content-app/
 ├─ content/
 ├─ pages/
 ├─ ...
```

Inside `content`, create a couple of Markdown files:

- `content/hello.md`:
  ```md
  # Hello World

  This is a sample markdown document stored in the content directory.
  ```

- `content/about.md`:
  ```md
  # About This Site

  This site demonstrates how to use Nuxt Content to fetch and display markdown.
  ```

### 4. Query Content in a Page

Now we’ll create a page that fetches and displays one of these documents. Nuxt Content provides composables like `useContent()` to query your markdown files.

Create `pages/index.vue`:
```vue
<!-- pages/index.vue -->
<template>
  <div>
    <h1>Nuxt Content Demo</h1>
    <p>This page will display content from <strong>hello.md</strong>:</p>

    <!-- Displaying the fetched markdown content -->
    <div v-html="docContent" />
  </div>
</template>

<script setup>
import { useAsyncData } from '#app'
import { queryContent } from '#content'

// Fetching the "hello.md" document content
const { data: doc } = await useAsyncData('hello-doc', () => 
  queryContent('hello').findOne()
)

// doc.value will be the content object from hello.md
const docContent = doc.value ? doc.value.body : 'Loading...'
</script>
```

- We use `queryContent('hello')` to find the `hello.md` document.
- `findOne()` returns the first matching document.
- `doc.value` now contains the parsed content, including `body`, which holds the HTML-rendered markdown.
- We then insert `docContent` into the template using `v-html` to render the markdown as HTML.

### 5. Run the Development Server

```bash
npm run dev
```

Open `http://localhost:3000` in your browser. You should see the `Hello World` heading and the corresponding text from `hello.md` displayed.

### 6. Creating a Dynamic Page for Other Documents (Optional)
You can also create a dynamic page to display any markdown file by name. For example, `pages/[slug].vue`:

```vue
<!-- pages/[slug].vue -->
<template>
  <div>
    <h1>{{ doc?.title }}</h1>
    <div v-html="doc?.body" />
  </div>
</template>

<script setup>
import { useAsyncData } from '#app'
import { queryContent } from '#content'
import { useRoute } from '#app'

const route = useRoute()
const slug = route.params.slug

const { data } = await useAsyncData(`content-${slug}`, () =>
  queryContent(slug).findOne()
)

const doc = data.value
</script>
```

Now, if you navigate to `http://localhost:3000/about`, it will display `about.md` automatically.

### 7. Further Enhancements
- Add more markdown files to `content/`.
- Experiment with frontmatter in your markdown, e.g.:
  ```md
  ---
  title: "Hello World Document"
  date: 2023-01-01
  ---
  
  # Hello World
  Some content here.
  ```
- Access frontmatter fields via `doc.value` to display metadata.
- Add styling and layouts for a nicer presentation.

- Nuxt Content allows you to store markdown files in `content` and query them using `queryContent()`.
- The returned object provides `body` as HTML, making it easy to insert into your pages.
- Using Nuxt’s file-based routing and composables, you can quickly build a static-site-like experience with dynamic content served from markdown files.

This demonstrates how to integrate Nuxt Content, place markdown files in the `content` directory, query them, and display their content on your Nuxt pages. 
