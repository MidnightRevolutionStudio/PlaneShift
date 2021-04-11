import { IAttribute } from "Interface/IAttribute";
import { Serializable } from "./Serializable";

export class Attribute extends Serializable implements IAttribute {
    name: string;
    value: number;

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }
}
