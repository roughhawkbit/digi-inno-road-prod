import torch

class DocumentAttention(torch.nn.Module):
    """
    Learns to dynamically weight the importance of the 7 different
    qualitative responses for a single firm.
    """
    def __init__(self, hidden_size):
        super().__init__()
        # W matrix for context mapping
        self.attention_weights = torch.nn.Linear(hidden_size, hidden_size)
        # c vector for scoring
        self.context_vector = torch.nn.Linear(hidden_size, 1, bias=False)

    def forward(self, hidden_states):
        # hidden_states shape: (batch_size, num_questions, hidden_size)

        # 1. Non-linear transformation
        u = torch.tanh(self.attention_weights(hidden_states))

        # 2. Calculate attention scores and apply softmax
        # attention_scores shape: (batch_size, num_questions, 1)
        attention_scores = self.context_vector(u)
        attention_weights = torch.softmax(attention_scores, dim=1)

        # 3. Compute weighted sum of the hidden states
        # aggregated_vector shape: (batch_size, hidden_size)
        aggregated_vector = torch.sum(attention_weights * hidden_states, dim=1)

        return aggregated_vector, attention_weights
    