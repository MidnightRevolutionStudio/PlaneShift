import React from "react"
import ReactDOM from "react-dom"
import { Subrace } from "./Class/Subrace";

class App extends React.Component {

    render() {
        var jsonHighElf: string = '{\n"name": "High Elf",\n"race": "Elf",\n"description": "As a high elf, you have a keen mind and a mastery of at least the basics of magic. In many fantasy gaming worlds, there are two kinds of high elves. One type is haughty and reclusive, believing themselves to be superior to non-elves and even other elves. The other type is more common and more friendly, and often encountered among humans and other races.",\n"attributeMods": [\n{\n"name": "INT",\n"value": 1\n}\n]\n}';
        var subrace: Subrace = new Subrace(jsonHighElf);

        return (
            <div>
                {subrace.name}<br />
                {subrace.race}<br />
                {subrace.attributeMods[0].name}: {subrace.attributeMods[0].value}<br />
                <br />
                {subrace.description}
            </div>
        );
    }
    SubraceTest(jsonStr: string) {
        var subrace: Subrace = new Subrace(jsonStr);
        return subrace;
    }
}

ReactDOM.render(<App />, document.getElementById("root"));