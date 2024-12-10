Instructions to set up a simple Nuxt 3 application that demonstrates basic routing, layouts, and reusable components. We’ll create a few pages to show navigation, introduce a shared layout, and use a reusable component within those pages.

**Steps:**

### 1. Create a New Nuxt 3 Project
Use the official Nuxt CLI (nuxi) to scaffold a new project:
```bash
npx nuxi init my-nuxt-app
```
This creates a `my-nuxt-app` directory with the Nuxt 3 starter template.

Move into the project directory:
```bash
cd my-nuxt-app
```

Install dependencies:
```bash
npm install
```

### 2. Run the Development Server
To verify that everything is working initially:
```bash
npm run dev
```
Open the URL shown in the terminal (usually `http://localhost:3000/`) to see the default Nuxt welcome page.

### 3. Create a Few Pages
Nuxt uses a file-based routing system. Pages are created inside the `pages` directory. We’ll create three pages: `index.vue`, `about.vue`, and `contact.vue`.

- `pages/index.vue` (Home Page):
  ```vue
  <template>
    <div>
      <h1>Home Page</h1>
      <p>Welcome to the home page!</p>
      <nav>
        <ul>
          <li><NuxtLink to="/about">Go to About</NuxtLink></li>
          <li><NuxtLink to="/contact">Go to Contact</NuxtLink></li>
        </ul>
      </nav>
    </div>
  </template>
  ```

- `pages/about.vue`:
  ```vue
  <template>
    <div>
      <h1>About Page</h1>
      <p>This is the about page of our Nuxt app.</p>
      <nav>
        <ul>
          <li><NuxtLink to="/">Home</NuxtLink></li>
          <li><NuxtLink to="/contact">Contact</NuxtLink></li>
        </ul>
      </nav>
    </div>
  </template>
  ```

- `pages/contact.vue`:
  ```vue
  <template>
    <div>
      <h1>Contact Page</h1>
      <p>Get in touch with us via the contact page!</p>
      <nav>
        <ul>
          <li><NuxtLink to="/">Home</NuxtLink></li>
          <li><NuxtLink to="/about">About</NuxtLink></li>
        </ul>
      </nav>
    </div>
  </template>
  ```

Now you have three pages, and you can navigate between them using `<NuxtLink>` components.

### 4. Add a Layout
Layouts let you define a common structure shared by all pages. For example, you might want a common header or footer on every page.

Create a `layouts` directory at the project root:
```
my-nuxt-app/
 ├─ layouts/
 ├─ pages/
 ├─ ...
```

Inside `layouts`, create a file named `default.vue`:
```vue
<!-- layouts/default.vue -->
<template>
  <div class="layout">
    <header>
      <h2>My Nuxt App</h2>
    </header>
    <!-- NuxtPage renders the page component here -->
    <NuxtPage />
    <footer>
      <p>© 2023 My Nuxt App</p>
    </footer>
  </div>
</template>
```

By default, all pages use the `default.vue` layout if none is specified. Now your pages will have a common header and footer.

### 5. Create a Reusable Component
Let’s create a simple reusable component that displays a stylized title. We’ll call it `MyTitle.vue`.

Create a `components` directory:
```
my-nuxt-app/
 ├─ components/
 ├─ layouts/
 ├─ pages/
 ├─ ...
```

Inside `components`, create `MyTitle.vue`:
```vue
<!-- components/MyTitle.vue -->
<template>
  <h1 :style="titleStyle">
    {{ text }}
  </h1>
</template>

<script setup>
const props = defineProps({
  text: {
    type: String,
    required: true
  }
})

const titleStyle = {
  color: 'blue',
  fontFamily: 'sans-serif'
}
</script>
```

This component takes a `text` prop and displays it in a styled `<h1>`.

### 6. Use the Component in a Page
Open one of your pages, for example `pages/index.vue`, and replace its `<h1>` with `<MyTitle>`:
```vue
<!-- pages/index.vue -->
<template>
  <div>
    <!-- Using our MyTitle component -->
    <MyTitle text="Home Page" />

    <p>Welcome to the home page!</p>
    <nav>
      <ul>
        <li><NuxtLink to="/about">Go to About</NuxtLink></li>
        <li><NuxtLink to="/contact">Go to Contact</NuxtLink></li>
      </ul>
    </nav>
  </div>
</template>

<script setup>
import MyTitle from '~/components/MyTitle.vue'
</script>
```

We imported the component and used it in the template. Now the home page title is rendered by a reusable component.

### 7. Check the Results

Run the development server:
```bash
npm run dev
```

Visit `http://localhost:3000`:
- You’ll see the header and footer from the `default.vue` layout.
- The Home Page title is styled by the `MyTitle` component.
- Navigation links let you move between Home, About, and Contact pages, all sharing the common layout.

### 8. Optional Enhancements
- Try using the `MyTitle` component on the about or contact pages as well.
- Add some global styling by creating a `app.vue` or configuring CSS in Nuxt.
- Experiment with another layout (e.g., `layouts/alternate.vue`) and assign it to one of the pages by adding `definePageMeta({ layout: 'alternate' })` in that page’s script section.

- **Routing:** Nuxt auto-generates routes from the `pages` directory. Each `.vue` file in `pages` is a route.
- **Layouts:** Putting a `default.vue` file in `layouts` applies a shared layout to all pages.
- **Components:** Creating a `components` directory and importing components into pages allows for reusable UI elements, promoting code reuse and consistency.

This setup gives you a small, functional Nuxt app that demonstrates basic routing, a shared layout, and reusable components, forming a foundation for more complex projects.
