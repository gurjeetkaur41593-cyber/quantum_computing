import cirq
import numpy as np

# --------------------------------------------------
# Generate Oracle Matrix for n input qubits
# --------------------------------------------------
def generate_oracle(n, function_values):

    size = 2 ** (n + 1)
    oracle_matrix = np.zeros((size, size))

    for x in range(2 ** n):
        for y in range(2):

            input_index = x * 2 + y

            fx = function_values[x]

            output_y = y ^ fx

            output_index = x * 2 + output_y

            oracle_matrix[input_index][output_index] = 1

    return cirq.MatrixGate(oracle_matrix)


# --------------------------------------------------
# Deutsch–Jozsa Circuit
# --------------------------------------------------
def deutsch_jozsa(n, oracle_gate):

    qubits = cirq.LineQubit.range(n + 1)

    circuit = cirq.Circuit()

    # Put output qubit in |1>
    circuit.append(cirq.X(qubits[n]))

    # Apply Hadamard to all qubits
    circuit.append(cirq.H.on_each(*qubits))

    # Apply Oracle
    circuit.append(oracle_gate(*qubits))

    # Apply Hadamard to input qubits only
    circuit.append(cirq.H.on_each(*qubits[:n]))

    # Measure input qubits
    circuit.append(cirq.measure(*qubits[:n], key='result'))

    return circuit


# --------------------------------------------------
# Determine function type
# --------------------------------------------------
def determine_type(result, n):

    measurements = result.measurements['result'][0]

    if all(bit == 0 for bit in measurements):
        return "Constant"
    else:
        return "Balanced"


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------
n = int(input("Enter number of input qubits (n): "))

total_values = 2 ** n

print(f"Enter {total_values} values (0 or 1) separated by commas:")

function_values = list(map(int, input().split(',')))

if len(function_values) != total_values:
    raise ValueError(f"You must enter exactly {total_values} values.")


# --------------------------------------------------
# Run Algorithm
# --------------------------------------------------
oracle_gate = generate_oracle(n, function_values)

circuit = deutsch_jozsa(n, oracle_gate)

simulator = cirq.Simulator()

result = simulator.run(circuit)

print("\nMeasurement:")
print(result)

function_type = determine_type(result, n)

print("\nFunction type:", function_type)

print("\nCircuit:")
print(circuit)