import { useEffect, useState } from 'react';
import { supabase, type Task } from './lib/supabase';
import { TaskForm } from './components/TaskForm';
import { TaskList } from './components/TaskList';
import { CheckSquare } from 'lucide-react';

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      setError('');
      const { data, error: fetchError } = await supabase
        .from('tasks')
        .select('*')
        .order('created_at', { ascending: false });

      if (fetchError) throw fetchError;
      setTasks(data || []);
    } catch (err) {
      setError('Failed to load tasks. Please refresh the page.');
      console.error('Error fetching tasks:', err);
    } finally {
      setLoading(false);
    }
  };

  const createTask = async (title: string, description: string) => {
    const { data, error: insertError } = await supabase
      .from('tasks')
      .insert([{ title, description, status: 'pending' }])
      .select()
      .single();

    if (insertError) throw insertError;
    if (data) {
      setTasks([data, ...tasks]);
    }
  };

  const updateTaskStatus = async (id: string, status: 'pending' | 'completed') => {
    try {
      const { error: updateError } = await supabase
        .from('tasks')
        .update({ status })
        .eq('id', id);

      if (updateError) throw updateError;

      setTasks(tasks.map((task) => (task.id === id ? { ...task, status } : task)));
    } catch (err) {
      setError('Failed to update task status.');
      console.error('Error updating task:', err);
    }
  };

  const deleteTask = async (id: string) => {
    try {
      const { error: deleteError } = await supabase.from('tasks').delete().eq('id', id);

      if (deleteError) throw deleteError;

      setTasks(tasks.filter((task) => task.id !== id));
    } catch (err) {
      setError('Failed to delete task.');
      console.error('Error deleting task:', err);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-gray-100">
      <div className="max-w-4xl mx-auto px-4 py-8">
        <header className="mb-8 text-center">
          <div className="flex items-center justify-center gap-3 mb-2">
            <CheckSquare size={36} className="text-blue-600" />
            <h1 className="text-4xl font-bold text-gray-900">DevTask Tracker</h1>
          </div>
          <p className="text-gray-600">Manage your development tasks efficiently</p>
        </header>

        {error && (
          <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700">
            {error}
          </div>
        )}

        <TaskForm onSubmit={createTask} />
        <TaskList
          tasks={tasks}
          loading={loading}
          onUpdateStatus={updateTaskStatus}
          onDelete={deleteTask}
        />
      </div>
    </div>
  );
}

export default App;
