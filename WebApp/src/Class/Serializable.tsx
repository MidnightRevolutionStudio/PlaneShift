export abstract class Serializable {
    constructor(jsonStr: string) {
        Object.assign(this, JSON.parse(jsonStr));
    }

    abstract Serialize(): string;
}
