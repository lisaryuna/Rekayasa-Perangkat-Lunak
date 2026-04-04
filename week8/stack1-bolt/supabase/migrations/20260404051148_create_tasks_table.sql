/*
  # Create Tasks Table

  1. New Tables
    - `tasks`
      - `id` (uuid, primary key) - Unique identifier for each task
      - `title` (text, required) - Task title
      - `description` (text, optional) - Task description
      - `status` (text, default 'pending') - Task status (pending/completed)
      - `created_at` (timestamptz) - Timestamp when task was created

  2. Security
    - Enable RLS on `tasks` table
    - Add policy for anyone to read all tasks
    - Add policy for anyone to insert tasks
    - Add policy for anyone to update tasks
    - Add policy for anyone to delete tasks

  Note: This implementation allows public access for simplicity.
  In production, these policies should be restricted to authenticated users.
*/

CREATE TABLE IF NOT EXISTS tasks (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  title text NOT NULL,
  description text DEFAULT '',
  status text DEFAULT 'pending' CHECK (status IN ('pending', 'completed')),
  created_at timestamptz DEFAULT now()
);

ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can read tasks"
  ON tasks FOR SELECT
  USING (true);

CREATE POLICY "Anyone can insert tasks"
  ON tasks FOR INSERT
  WITH CHECK (true);

CREATE POLICY "Anyone can update tasks"
  ON tasks FOR UPDATE
  USING (true)
  WITH CHECK (true);

CREATE POLICY "Anyone can delete tasks"
  ON tasks FOR DELETE
  USING (true);