# Pygen

**Pygen** is an unofficial Python-based interpreter for the esoteric language [Protogen](https://esolangs.org/wiki/Protogen). Protogen itself is not exactly user-friendly, and while Pygen makes things easier compared to the official interpreter, it’s still far from straightforward. If you're after a smoother experience, stick with more accessible languages like [Python](https://www.python.org/) or [BASIC](http://www.quitebasic.com/). Esoteric languages like Protogen are not known for being intuitive, and there are some, like [Malbolge](https://esolangs.org/wiki/Malbolge) and [BrainF](https://esolangs.org/wiki/BrainF), that are even more difficult.

## Key Differences Between Pygen and the Official Interpreter

One notable difference is that Pygen simplifies file handling. Unlike the official Protogen interpreter, you don’t need to manually specify the path to a program file. Pygen lets you run any of the [example programs](https://github.com/UniqueName12345/Pygen/tree/main/examples) included in the repository without worrying about file paths. You can also create your own Protogen programs, but be prepared for a potentially time-consuming debugging process (especially if you forget to add something like a null byte in a key position).

## Bytogen (Work in Progress)

For a slightly more approachable experience, Pygen introduces a feature called **Bytogen view**. Bytogen view converts the byte-level representation of a Protogen program into readable characters, helping you make sense of the underlying code. However, keep in mind that Bytogen can't yet be compiled back into Protogen, so always keep a backup of your original Protogen program.

To work with Bytogen, you'll still need to work with Protogen, which in order to work with Protogen, you'll need a hex editor, such as [HxD](https://mh-nexus.de/en/hxd/) or the [Hex Editor extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-vscode.hexeditor).
