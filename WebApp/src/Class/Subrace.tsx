import { Attribute } from "./Attribute";
import { Serializable } from "./Serializable";

export class Subrace extends Serializable {
    name: string;
    race: string;
    description: string;
    attributeMods: Attribute[];

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }
}
