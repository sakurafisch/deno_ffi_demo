(function main() {
    let libName = "";
    switch (Deno.build.os) {
        case "windows":
            libName = "./add.dll";
            break;
        case "darwin":
            libName = "./add.dylib";
            break;
        default:
            libName = "./libadd.so";
            break;
    }

    const dylib = Deno.dlopen(
        libName,
        {
            "add": {parameters: ["isize", "isize"],result: "isize"}
        } as const,
    );

    const result = dylib.symbols.add(35, 34);

    console.log(`Result from external addition of 35 and 34: ${result}`);
})();
