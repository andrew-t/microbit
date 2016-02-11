# micro:bit code generator

## micro:bit "Javascript" limitations

* You can't call a function.
* You must always use braces around `if` statements etc — in particular you cannot use `else if`. You must use `else { if ... }`
* You can't use `switch`.
* Variables are treated as strongly typed.
* You can't use arrays or objects.
* You can't use increment operators, even in for loops. Use `i = i + 1`.
* You can't declare variables outside a function; put them on `globals`.
* You can't declare variables without also assigning them.
* You can't declare two variables on one line (`var a = 1, b = 2;`).
* You can't use non-integer numbers. `3/2 == 1`.

## Generator limitations:

You can call functions now, but they *must* be written exactly as so:

```
function functionName() {
	// code goes here
}
```

You cannot pass arguments to a function. You cannot make functions recursive, even in unreachable code paths, as they are inlined.

You cannot place two statements on a line if they need re-writing (eg, function calls).

## Future ideas

Using a real lexer/parser, we could:

* polyfill function arguments;
* remove syntax limitations.
