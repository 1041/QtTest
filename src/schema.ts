import { z } from 'zod';

export const UserSchema = z.object({
  name: z.string().min(1, { message: 'Name is required' }),
  email: z.string().min(1, { message: 'Email is required' }),
  age: z.number().min(18, { message: 'Must be 18 or older' }),
});
