import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('');

  // Ini alamat backend FastAPI kamu
  const API_URL = "http://127.0.0.1:8000/tasks";

  const fetchTasks = async () => {
    try {
      const res = await axios.get(API_URL);
      setTasks(res.data);
    } catch (error) {
      console.error("Backend belum nyala atau error:", error);
    }
  };

  useEffect(() => { fetchTasks(); }, []);

  const addTask = async (e) => {
    e.preventDefault();
    if (!title) return alert("Judul wajib diisi!");
    
    await axios.post(API_URL, { title, description: desc });
    setTitle(''); 
    setDesc('');
    fetchTasks();
  };

  const deleteTask = async (id) => {
    await axios.delete(`${API_URL}/${id}`);
    fetchTasks();
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial', maxWidth: '600px', margin: '0 auto' }}>
      <h1>DevTask Tracker (FastAPI + React)</h1>
      
      <form onSubmit={addTask} style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginBottom: '20px', padding: '15px', border: '1px solid #ccc', borderRadius: '5px' }}>
        <input 
          placeholder="Judul Tugas *" 
          value={title} 
          onChange={(e) => setTitle(e.target.value)} 
          style={{ padding: '8px' }}
        />
        <input 
          placeholder="Deskripsi (Opsional)" 
          value={desc} 
          onChange={(e) => setDesc(e.target.value)} 
          style={{ padding: '8px' }}
        />
        <button type="submit" style={{ padding: '10px', background: '#007BFF', color: 'white', border: 'none', cursor: 'pointer' }}>
          Tambah Tugas
        </button>
      </form>

      <ul style={{ listStyleType: 'none', padding: 0 }}>
        {tasks.map(t => (
          <li key={t.id} style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px', padding: '10px', borderBottom: '1px solid #eee' }}>
            <div>
              <strong style={{ display: 'block' }}>{t.title}</strong>
              <span style={{ fontSize: '14px', color: '#666' }}>{t.description}</span>
            </div>
            <button onClick={() => deleteTask(t.id)} style={{ background: '#dc3545', color: 'white', border: 'none', padding: '5px 10px', cursor: 'pointer' }}>
              Hapus
            </button>
          </li>
        ))}
        {tasks.length === 0 && <p>Belum ada tugas. Yuk buat baru!</p>}
      </ul>
    </div>
  );
}

export default App;