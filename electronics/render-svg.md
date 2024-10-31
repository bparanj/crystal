I'll show you how to render SVG on a web page using different methods:



```html
<!-- Method 1: Direct SVG in HTML -->
<!DOCTYPE html>
<html>
<head>
    <title>SVG Examples</title>
    <style>
        .svg-container {
            margin: 20px;
            border: 1px solid #ccc;
            padding: 10px;
        }
    </style>
</head>
<body>
    <!-- Method 1: Inline SVG -->
    <div class="svg-container">
        <h3>Method 1: Inline SVG</h3>
        <svg width="200" height="100" viewBox="0 0 200 100">
            <circle cx="50" cy="50" r="40" stroke="black" stroke-width="2" fill="red"/>
        </svg>
    </div>

    <!-- Method 2: Using img tag -->
    <div class="svg-container">
        <h3>Method 2: SVG as Image</h3>
        <img src="circle.svg" alt="Circle SVG" width="200" height="100">
    </div>

    <!-- Method 3: Using object tag -->
    <div class="svg-container">
        <h3>Method 3: SVG as Object</h3>
        <object data="circle.svg" type="image/svg+xml" width="200" height="100"></object>
    </div>

    <!-- Method 4: Using embed tag -->
    <div class="svg-container">
        <h3>Method 4: SVG using Embed</h3>
        <embed src="circle.svg" type="image/svg+xml" width="200" height="100">
    </div>
</body>
</html>

<!-- Example circle.svg file content -->
<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="100" viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="50" r="40" stroke="black" stroke-width="2" fill="red"/>
</svg>

```

Here are the main methods to render SVG on a web page:

1. Inline SVG (Method 1):
- Directly embed SVG code in HTML
- Best for:
  - Dynamic manipulation with JavaScript
  - Styling with CSS
  - Small, simple SVGs
```html
<svg width="200" height="100">
    <!-- SVG content here -->
</svg>
```

2. Using img tag (Method 2):
- Treat SVG as an image file
- Best for:
  - Static images
  - Simple implementation
```html
<img src="image.svg" alt="SVG image">
```

3. Using object tag (Method 3):
- More flexible than img
- Allows interaction
```html
<object data="image.svg" type="image/svg+xml"></object>
```

4. Using embed tag (Method 4):
- Similar to object tag
- Older method, still supported
```html
<embed src="image.svg" type="image/svg+xml">
```

Additional Tips:
1. For responsive SVG:
```css
svg {
    width: 100%;
    height: auto;
}
```

2. To make SVG accessible:
- Add title and description tags
- Use ARIA labels
- Include meaningful alt text

Would you like me to explain more about any of these methods or show how to manipulate SVGs dynamically with JavaScript?

<!-- Method 1: Direct SVG in HTML -->
<!DOCTYPE html>
<html>
<head>
    <title>SVG Examples</title>
    <style>
        .svg-container {
            margin: 20px;
            border: 1px solid #ccc;
            padding: 10px;
        }
    </style>
</head>
<body>
    <!-- Method 1: Inline SVG -->
    <div class="svg-container">
        <h3>Method 1: Inline SVG</h3>
        <svg width="200" height="100" viewBox="0 0 200 100">
            <circle cx="50" cy="50" r="40" stroke="black" stroke-width="2" fill="red"/>
        </svg>
    </div>

    <!-- Method 2: Using img tag -->
    <div class="svg-container">
        <h3>Method 2: SVG as Image</h3>
        <img src="circle.svg" alt="Circle SVG" width="200" height="100">
    </div>

    <!-- Method 3: Using object tag -->
    <div class="svg-container">
        <h3>Method 3: SVG as Object</h3>
        <object data="circle.svg" type="image/svg+xml" width="200" height="100"></object>
    </div>

    <!-- Method 4: Using embed tag -->
    <div class="svg-container">
        <h3>Method 4: SVG using Embed</h3>
        <embed src="circle.svg" type="image/svg+xml" width="200" height="100">
    </div>
</body>
</html>

<!-- Example circle.svg file content -->
<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="100" viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="50" r="40" stroke="black" stroke-width="2" fill="red"/>
</svg>
