enum ProficiencyLevel {
    None = 0,
    Proficient,
    Expertise
}

interface IProficiency {
    name: string;
    level: number;
}