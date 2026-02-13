import cirq
import numpy as np

# -----------------------------------------
# Generate Oracle from 4 Boolean values
# -----------------------------------------
def generate_oracle_from_function():
    print("Enter 4 values for f(00), f(01), f(10), f(11) separated by commas (0 or 1):")
    values = list(map(int, input().strip().split(',')))

    if len(values) != 4 or any(v not in [0, 1] for v in values):
        raise ValueError("You must enter exactly 4 values (0 or 1).")

    oracle_matrix = np.zeros((8, 8))

    for x in range(4):  # 00,01,10,11
        for y in range(2):  # 0 or 1
            input_index = x * 2 + y
            fx = values[x]
            output_y = y ^ fx
            output_index = x * 2 + output_y
            oracle_matrix[input_index][output_index] = 1

    return cirq.MatrixGate(oracle_matrix)


# -----------------------------------------
# Deutsch–Jozsa Circuit
# -----------------------------------------
def deutsch_jozsa_algorithm(oracle_gate):

    # 2 input qubits + 1 output qubit
    qubits = cirq.LineQubit.range(3)

    circuit = cirq.Circuit()

    # Step 1: Put output qubit in |1>
    circuit.append(cirq.X(qubits[2]))

    # Step 2: Apply Hadamard to ALL qubits
    circuit.append([cirq.H(q) for q in qubits])

    # Step 3: Apply Oracle
    circuit.append(oracle_gate(*qubits))

    # Step 4: Apply Hadamard ONLY to input qubits
    circuit.append([cirq.H(qubits[0]), cirq.H(qubits[1])])

    # Step 5: Measure input qubits
    circuit.append([
        cirq.measure(qubits[0], key='result_0'),
        cirq.measure(qubits[1], key='result_1')
    ])

    return circuit


# -----------------------------------------
# Determine function type
# -----------------------------------------
def determine_function_type(result):
    m0 = result.measurements['result_0'][0][0]
    m1 = result.measurements['result_1'][0][0]

    if m0 == 0 and m1 == 0:
        return "Constant"
    else:
        return "Balanced"


# -----------------------------------------
# MAIN
# -----------------------------------------
oracle_gate = generate_oracle_from_function()

circuit = deutsch_jozsa_algorithm(oracle_gate)

simulator = cirq.Simulator()
result = simulator.run(circuit)

print("\nMeasurement results:")
print(result)

function_type = determine_function_type(result)
print("\nFunction type:", function_type)

print("\nCircuit:")
print(circuit)