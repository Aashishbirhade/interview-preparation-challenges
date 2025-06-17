import react from 'react';
import Child from './child';

function Parent() {
    return(
        <div>
            <h1>Parent Component</h1>
            <Child name="John Doe" age={30} />
        </div>
    );
}
export default Parent;