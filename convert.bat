@echo off

REM Check if node_modules exists
IF NOT EXIST "node_modules" (
    echo "Node modules not found. Installing dependencies..."
    call npm install
)

REM Run the conversion script
echo "Converting Zod schema to JSON Schema..."
call npx ts-node src/convert-schema.ts

echo "Conversion complete."
pause
