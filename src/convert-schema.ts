import { zodToJsonSchema } from 'zod-to-json-schema';
import { UserSchema } from './schema';
import * as fs from 'fs';
import * as path from 'path';

const jsonSchema = zodToJsonSchema(UserSchema, "UserSchema");

const outputPath = path.resolve(__dirname, '../schema.json');
fs.writeFileSync(outputPath, JSON.stringify(jsonSchema, null, 2));

console.log(`✅ JSON Schema has been generated at ${outputPath}`);
