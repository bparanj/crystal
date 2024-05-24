This article consists of the following:

1. Creating a new Nuxt 3 app
2. Navigating to different pages using NuxtLink component.

Create a Nuxt 3 app:

```
npx nuxi init hw
```

Create home page:

```
npx nuxi add page index
```

Create a login page.

Create a navigation bar.

In app.vue:

Change this:

```html
<template>
  <div>
    <NuxtPage />
  </div>
</template>
```

to:

```html
<template>
  <div>
		<nav>
			<NuxtLink to="/"> Home </NuxtLink>
			<NuxtLink to="/login"> Login </NuxtLink>
		</nav>	
    <NuxtPage />
  </div>
</template>
```