# Chapter 8: Make It Pretty

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

**Taking a screenshot:** `Cmd+Ctrl+Shift+4` → drag to select area → copies to clipboard

**Paste into Claude Code:** `Cmd+V`

Share your screenshot:

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
The progress bar is printing multiple lines instead of updating in place. Fix it to overwrite the same line.
```

```
Can you add a blinking cursor effect when paused?
```

## Commit the Pretty Version

Once you're happy with the visual adjustments:

```
commit these changes
```

---

[Next: Chapter 9 - Custom Automation →](09-custom-automation.md)

---

## Skills Learned

- [ ] Screenshot as feedback
- [ ] Image input for design reference
- [ ] Iterating visually

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 7: Context Mastery](07-context-mastery.md) | [README](../README.md) | [Chapter 9: Custom Automation](09-custom-automation.md) |
