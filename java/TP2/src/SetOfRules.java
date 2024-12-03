public class SetOfRules {
    private Rule[] rules;

    public SetOfRules(Rule[] rules) {
        this.rules = rules;
    }

    public String apply(String sequence) {
        StringBuilder result = new StringBuilder();
        
        for (char c : sequence.toCharArray()) {
            boolean replaced = false;
            for (Rule rule : rules) {
                if (rule.getSymbol() == c) {
                    result.append(rule.getSequence());
                    replaced = true;
                    break;
                }
            }
            if (!replaced) {
                result.append(c);
            }
        }
        
        return result.toString();
    }
}
