import { Check, Trash2, X } from 'lucide-react';
import type { Task } from '../lib/supabase';

interface TaskItemProps {
  task: Task;
  onUpdateStatus: (id: string, status: 'pending' | 'completed') => Promise<void>;
  onDelete: (id: string) => Promise<void>;
}

export function TaskItem({ task, onUpdateStatus, onDelete }: TaskItemProps) {
  const isCompleted = task.status === 'completed';

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-4 hover:shadow-md transition-shadow">
      <div className="flex items-start justify-between gap-4">
        <div className="flex-1 min-w-0">
          <h3
            className={`text-lg font-medium ${
              isCompleted ? 'text-gray-500 line-through' : 'text-gray-900'
            }`}
          >
            {task.title}
          </h3>
          {task.description && (
            <p className={`mt-1 text-sm ${isCompleted ? 'text-gray-400' : 'text-gray-600'}`}>
              {task.description}
            </p>
          )}
          <div className="mt-2 flex items-center gap-2">
            <span
              className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                isCompleted
                  ? 'bg-green-100 text-green-800'
                  : 'bg-yellow-100 text-yellow-800'
              }`}
            >
              {isCompleted ? 'Completed' : 'Pending'}
            </span>
            <span className="text-xs text-gray-500">
              {new Date(task.created_at).toLocaleDateString()}
            </span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={() => onUpdateStatus(task.id, isCompleted ? 'pending' : 'completed')}
            className={`p-2 rounded-md transition-colors ${
              isCompleted
                ? 'bg-yellow-100 hover:bg-yellow-200 text-yellow-700'
                : 'bg-green-100 hover:bg-green-200 text-green-700'
            }`}
            title={isCompleted ? 'Mark as pending' : 'Mark as completed'}
          >
            {isCompleted ? <X size={18} /> : <Check size={18} />}
          </button>
          <button
            onClick={() => onDelete(task.id)}
            className="p-2 bg-red-100 hover:bg-red-200 text-red-700 rounded-md transition-colors"
            title="Delete task"
          >
            <Trash2 size={18} />
          </button>
        </div>
      </div>
    </div>
  );
}
