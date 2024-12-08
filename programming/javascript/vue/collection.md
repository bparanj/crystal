Below is an exercise designed to help you practice using the `$content` API (Nuxt Content v1, typically used in Nuxt 2) to retrieve and display a list of articles. You will create a Nuxt page that queries a collection of Markdown files from the `content/` directory and then render a list of article titles on the page.

**Prerequisites:**
- A Nuxt 2.x project with the Nuxt Content module installed and configured.
- Basic understanding of Nuxt pages, the `content/` directory, and the `$content` API.

**If you have not set up Nuxt Content yet:**
1. Install Nuxt Content:  
   ```bash
   npm install @nuxt/content
   ```
2. Add `@nuxt/content` to `modules` in `nuxt.config.js`:
   ```js
   // nuxt.config.js
   export default {
     buildModules: [
       '@nuxt/content'
     ]
   }
   ```

### Step-by-Step Exercise

1. **Create the `content` Directory and Articles:**
   Inside the root of your project, create a `content` directory if it doesn’t exist:
   ```
   project/
    ├─ content/
    ├─ pages/
    ├─ nuxt.config.js
   ```

   Add a few Markdown files to the `content` directory, for example:

   - `content/article1.md`:
     ```md
     ---
     title: "First Article"
     description: "An intro to our first article."
     ---

     # First Article

     This is the content of the first article.
     ```

   - `content/article2.md`:
     ```md
     ---
     title: "Second Article"
     description: "A quick look at the second article."
     ---

     # Second Article

     This is the content of the second article.
     ```

   Add a few more articles as needed. Each should have at least a `title` in the front matter.

2. **Create a Page to List Articles:**
   In your `pages/` directory, create a file named `articles.vue` (i.e., `pages/articles.vue`):
   ```vue
   <template>
     <div>
       <h1>Articles</h1>
       <ul>
         <li v-for="article in articles" :key="article.slug">
           <nuxt-link :to="`/articles/${article.slug}`">{{ article.title }}</nuxt-link>
         </li>
       </ul>
     </div>
   </template>

   <script>
   export default {
     async asyncData({ $content }) {
       // Query all articles in the content directory
       const articles = await $content().only(['title', 'slug']).sortBy('title', 'asc').fetch()

       return { articles }
     }
   }
   </script>
   ```

   **Explanation:**
   - `asyncData` is a special Nuxt hook that runs on the server before rendering the page, allowing you to fetch data.
   - `$content()` is the Nuxt Content API that queries the `content/` directory.
   - `.only(['title', 'slug'])` limits the fields we retrieve, so we get just the title and slug to display.
   - `.sortBy('title', 'asc')` sorts the articles by their title in ascending order.
   - `fetch()` actually performs the query and returns the results.
   - We return the `articles` array, which we then use to render a list of links in the template.
   - Each `<nuxt-link>` uses the article’s slug to link to a detail page (which we will create next).

3. **Create an Article Detail Page (Optional):**
   To view a single article’s content, create a dynamic page, for example `pages/articles/_slug.vue`:
   ```vue
   <template>
     <div>
       <h1>{{ article.title }}</h1>
       <nuxt-content :document="article" />
     </div>
   </template>

   <script>
   export default {
     async asyncData({ params, $content }) {
       const article = await $content(params.slug).fetch()
       return { article }
     }
   }
   </script>
   ```

   **Explanation:**
   - This page will match any route like `/articles/some-article`.
   - We fetch the article by using `$content(params.slug)` where `params.slug` is the dynamic parameter from the URL.
   - The `<nuxt-content :document="article" />` component renders the body of the markdown file.

4. **Run the Development Server:**
   If not already running:
   ```bash
   npm run dev
   ```
   
   Visit `http://localhost:3000/articles` in your browser. You should see a list of articles displayed by their titles. Clicking on any title should take you to its detail page.

5. **Enhance the Exercise:**
   - Add more metadata fields to the markdown front matter and display them in the list or on the detail page.
   - Filter articles by category or tag, adding fields to your markdown front matter and using `$content()` queries.
   - Add pagination if you have many articles, using `.limit()` and `.skip()` in your queries.

**Key Takeaways:**
- `$content()` is a powerful API to query markdown content stored in the `content/` directory.
- `asyncData` lets you fetch content on the server side before rendering.
- By using `$content`, you can quickly build a simple CMS-like feature where markdown files become your content source.
- The optional article detail page demonstrates how to link from a list view to a detail view using dynamic routes.

This exercise gives you a hands-on experience with `$content` to retrieve and display a list of articles, and lays the groundwork for building more complex content-driven Nuxt apps.
