# Chapter 5: Make It Pretty

The timer works, but it's ugly. Time to learn one of Claude Code's most powerful features: visual feedback.

## Screenshot as Feedback

Claude can see images. This means you can:
- Show Claude what your app currently looks like
- Show Claude what you *want* it to look like
- Iterate visually

## The Exercise

### Step 1: Screenshot the Current State

Run the timer:
```bash
python src/pomodoro.py start --minutes 1
```

Take a screenshot of your terminal showing the plain, ugly output.

<!-- SCREENSHOT: The ugly plain text timer -->

### Step 2: Share the Screenshot with Claude

In Claude Code, you can paste images directly or drag them in. Share your screenshot:

```
Here's what the timer currently looks like: [paste screenshot]

It's boring. Make it look better with:
- Colors
- A progress bar
- Maybe an ASCII tomato
```

Claude will see the image and understand exactly what you're starting from.

<!-- SCREENSHOT: Claude receiving and acknowledging the image -->

### Step 3: Show Inspiration (Optional)

If you have a specific look in mind, find an example online and share it:

```
Here's a CLI app I like the look of: [paste screenshot]

Make our timer look more like this style.
```

This is incredibly powerful. Instead of describing what you want in words, you show Claude directly.

## Iterating Visually

### The Feedback Loop

1. Claude makes changes
2. You run the app
3. You screenshot the result
4. You share with Claude: "Getting closer, but..."
5. Claude refines
6. Repeat

```
Here's what it looks like now: [paste screenshot]

The colors are good but the progress bar is too small.
Make it wider and add percentage.
```

### Example Prompts

```
The tomato emoji doesn't render in my terminal. Use ASCII art instead.
```

```
The red is too bright, use a softer color.
```

```
Can you add a blinking cursor effect when paused?
```

## What Claude Might Add

Depending on your prompts, the final timer might have:

- **Colors**: Using ANSI escape codes or a library like `colorama`
- **Progress bar**: Visual representation of time remaining
- **ASCII art**: A tomato made of characters
- **Clear screen**: Clean display that updates in place
- **Better formatting**: Centered text, borders, etc.

## Commit the Pretty Version

```
/commit
```

## Compare Before and After

Take a final screenshot. Compare it to Chapter 0.

<!-- SCREENSHOT: Before/after comparison -->

The app has gone from embarrassing to impressive—and you described most of it visually.

## Pro Tips

### Terminal Font Matters

Some ASCII art looks broken in certain fonts. If Claude's art doesn't render right, tell it:
```
My terminal uses [font name], the box-drawing characters aren't rendering.
Use simpler ASCII characters.
```

### Color Support Varies

Not all terminals support all colors:
```
My terminal doesn't support 256 colors, use basic ANSI colors only.
```

### Testing Visual Changes

Always run the app after visual changes. What looks good in theory might look broken in practice.

---

[Next: Chapter 6 - External Docs →](06-external-docs.md)

---

## Skills Learned

- [ ] Screenshot as feedback
- [ ] Image input for design reference
- [ ] Iterating visually
- [ ] Multi-file edits

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 4: Your First Feature](04-first-feature.md) | [README](../README.md) | [Chapter 6: External Docs](06-external-docs.md) |
