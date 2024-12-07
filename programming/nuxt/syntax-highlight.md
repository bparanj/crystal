Below are high-level instructions to add code syntax highlighting to your Nuxt Content project using Nuxt UI Pro components. Adjust paths and configurations according to your project’s structure.

**1. Install and Configure Nuxt UI Pro**  
   - Ensure you have access to Nuxt UI Pro.  
   - Follow the official documentation to install and register Nuxt UI Pro in your `nuxt.config.ts` file. For example:
     ```ts
     // nuxt.config.ts
     export default defineNuxtConfig({
       modules: [
         '@nuxt/ui' // Assuming you installed Nuxt UI Pro via its standard setup
       ]
     })
     ```

**2. Enable Syntax Highlighting in Nuxt Content**  
   - Nuxt Content can integrate with syntax highlighting libraries. Add the appropriate support in `nuxt.config.ts`.  
   - For example, if using Shiki (commonly recommended by Nuxt Content):
     ```ts
     // nuxt.config.ts
     export default defineNuxtConfig({
       content: {
         highlight: {
           theme: 'github-dark', // choose a theme or use 'github-light'
           preload: ['js', 'ts', 'bash', 'html', 'css'] // languages you want to highlight
         }
       }
     })
     ```
   - Nuxt Content will now automatically parse fenced code blocks in your Markdown and add syntax highlighting data.

**3. Using Nuxt UI Pro Code Components**  
   - Nuxt UI Pro typically provides pre-styled components for code blocks, for example `<NCodeBlock>` or `<NCode>` (check the Nuxt UI Pro docs for the exact component names).  
   - These components are designed to display code with nice formatting. If the Nuxt Content default rendering does not use these components out-of-the-box, you can override how Nuxt Content renders code blocks.

**4. Override the Default Content Rendering**  
   - Create or edit a `~/components/content/CodeBlock.vue` file (or similar) to wrap content code blocks in a Nuxt UI Pro code component.
   - Nuxt Content allows you to customize the rendering of different elements by using the `components` option. For example:
     ```vue
     <!-- ~/components/content/CodeBlock.vue -->
     <template>
       <NCodeBlock :code="props.code" :language="props.language" />
     </template>

     <script setup lang="ts">
     const props = defineProps({
       code: {
         type: String,
         required: true
       },
       language: {
         type: String,
         required: true
       }
     })
     </script>
     ```
   - In your `nuxt.config.ts`, map the default code renderer to this new component:
     ```ts
     // nuxt.config.ts
     export default defineNuxtConfig({
       content: {
         highlight: { ... }, // your highlighting config
         markdown: {
           // Map the default code block renderer to our CodeBlock component
           prism: false, // if you previously enabled it
           remarkPlugins: [],
           rehypePlugins: [],
           // components: Object of tag names to component names
           components: {
             code: 'CodeBlock' // Replace the default rendering of code blocks
           }
         }
       }
     })
     ```

**5. Confirm Proper Rendering**  
   - With the above configuration, when you place a fenced code block in a Markdown file inside your `content` directory, Nuxt Content will highlight it using Shiki.  
   - Your custom `CodeBlock.vue` component (which uses `<NCodeBlock>`) will receive the highlighted code and display it with Nuxt UI Pro’s styles.

**6. Adjusting Styles and Themes**  
   - Test different themes in the `highlight` configuration (e.g., `github-dark`, `dracula`, `nord`) to find one that matches your site’s look.  
   - Ensure that `<NCodeBlock>` or `<NCode>` components from Nuxt UI Pro are compatible with your theme. Some slight CSS adjustments might be needed.

---

**Key Takeaways**:  
- You configure Nuxt Content to handle syntax highlighting (e.g., via Shiki).  
- You override how code blocks are rendered by Nuxt Content so that they use Nuxt UI Pro’s code block component.  
- You tweak settings and themes until you have the desired syntax highlighting style and formatting.
