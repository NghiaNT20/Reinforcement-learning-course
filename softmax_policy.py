import numpy as np  # Import thư viện numpy để xử lý mảng và tính toán số học

class SoftmaxPolicy:
    def __init__(self, num_actions, temperature):
        """
        Khởi tạo chính sách Softmax.
        
        Parameters:
        - num_actions: số lượng hành động có thể chọn
        - temperature: tham số nhiệt độ để điều chỉnh tính xác suất của Softmax
        """
        self.num_actions = num_actions
        self.temperature = temperature

    def select_action(self, q_values):
        """
        Chọn một hành động dựa trên chính sách Softmax.

        Parameters:
        - q_values: mảng chứa giá trị Q của từng hành động

        Returns:
        - action: hành động được chọn theo xác suất Softmax
        """
        probabilities = self.softmax(q_values)  # Tính xác suất softmax
        action = np.random.choice(self.num_actions, p=probabilities)  # Chọn hành động dựa trên phân phối
        return action

    def softmax(self, q_values):
        """
        Tính toán phân phối xác suất Softmax dựa trên giá trị Q.

        Parameters:
        - q_values: mảng chứa giá trị Q của từng hành động

        Returns:
        - probabilities: mảng chứa xác suất của từng hành động
        """
        scaled_values = q_values / self.temperature  # Chia giá trị Q cho temperature để điều chỉnh độ sắc nét
        exp_values = np.exp(scaled_values)  # Tính hàm mũ của giá trị đã chia
        probabilities = exp_values / np.sum(exp_values)  # Chuẩn hóa thành xác suất
        return probabilities

# ----------- Ví dụ sử dụng ----------------

# Số lượng hành động có thể thực hiện (4 hướng: Lên, Xuống, Trái, Phải)
num_actions = 4
temperature = 0.5  # Điều chỉnh mức độ chọn lựa ngẫu nhiên

# Khởi tạo chính sách Softmax
softmax_policy = SoftmaxPolicy(num_actions, temperature)

# Ví dụ về giá trị Q của 4 hành động
q_values = np.array([1.0, 2.0, 0.5, 1.5])

# Chọn hành động dựa trên chính sách Softmax
selected_action = softmax_policy.select_action(q_values)

print("Selected Action:", selected_action)
