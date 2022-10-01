import "./App.css"
import Post from "./components/Post"
import { CreatePost } from './components/Post'

function App() {
  return (
    <div className="App">
      <Post />
      <CreatePost />
    </div>
  )
}

export default App
