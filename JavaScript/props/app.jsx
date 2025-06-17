import react from 'react';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Parent from './Parent';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Parent />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;