import numpy as np
from copy import copy
import numpy as np
from scipy.spatial.transform import Rotation as R

def dhreal(delta_config):
    # Posiciones y orientaciones absolutas de los frames
    # Lista de ejes (del 0 al 7)
    joints = [
        {"pos": [0, 0, 0], "quat": [0, 0, 0, 1], "type": None, "axis": None},  # Eje 0 (base)
        {"pos": [0.4, 1.17, 0.18], "quat": [0, 0, 0, 1], "type": "prismático", "axis": "y"},
        {"pos": [0, 0.475, 0.44], "quat": [0, 0, 0, 1], "type": "rotacional", "axis": "z"},
        {"pos": [0.74, -0.08, 0.15], "quat": [0, 0.333, 0, 0.94275], "type": "rotacional", "axis": "y"},
        {"pos": [0, -0.19, 1.15], "quat": [0, -0.703, 0, 0.711], "type": "rotacional", "axis": "y"},
        {"pos": [1.03, 0.27, 0.25], "quat": [0, 0, 0, 1], "type": "rotacional", "axis": "x"},
        {"pos": [0.19, -0.17, 0], "quat": [0, 0, 0, 1], "type": "rotacional", "axis": "y"},
        {"pos": [0.22, 0.13, 0], "quat": [0, 0, 0, 1], "type": "rotacional", "axis": "x"},
    ]


    # Configuración inicial real (desde joint_states)
    initial_config = np.array([1.17, 0.0, 0.68, 1.56, 0.0, 5.5e-05, 0.0])

    # Signos de giro reales: - + - + + - +
    signs = np.array([-1, 1, -1, 1, 1, -1, 1])

    # Configuración total aplicando dirección y desplazamiento
    q_total = initial_config + delta_config
    q_signed = signs * q_total

    T = np.eye(4)

    for i in range(1, len(joints)):
        joint = joints[i]
        p = np.array(joint["pos"])
        rot = R.from_quat(joint["quat"]).as_matrix()
        T_joint = np.eye(4)
        T_joint[:3, :3] = rot
        T_joint[:3, 3] = p

        T_mov = np.eye(4)

        if joint["type"] == "rotacional":
            angle = q_signed[i - 1]
            if joint["axis"] == "x":
                R_mov = R.from_rotvec([angle, 0, 0]).as_matrix()
            elif joint["axis"] == "y":
                R_mov = R.from_rotvec([0, angle, 0]).as_matrix()
            elif joint["axis"] == "z":
                R_mov = R.from_rotvec([0, 0, angle]).as_matrix()
            else:
                raise ValueError("Eje de rotación desconocido")
            T_mov[:3, :3] = R_mov

        elif joint["type"] == "prismático":
            d = q_signed[i - 1]
            if joint["axis"] == "x":
                T_mov[0, 3] = d
            elif joint["axis"] == "y":
                T_mov[1, 3] = d
            elif joint["axis"] == "z":
                T_mov[2, 3] = d
            else:
                raise ValueError("Eje prismatic desconocido")

        # Transformación acumulada
        T = T @ T_joint @ T_mov

    return T


cos=np.cos; sin=np.sin; pi=np.pi


def rot2quat(R):
 """
 Convertir una matriz de rotacion en un cuaternion

 Entrada:
  R -- Matriz de rotacion
 Salida:
  Q -- Cuaternion [ew, ex, ey, ez]

 """
 dEpsilon = 1e-6
 quat = 4*[0.,]

 quat[0] = 0.5*np.sqrt(R[0,0]+R[1,1]+R[2,2]+1.0)
 if ( np.fabs(R[0,0]-R[1,1]-R[2,2]+1.0) < dEpsilon ):
  quat[1] = 0.0
 else:
  quat[1] = 0.5*np.sign(R[2,1]-R[1,2])*np.sqrt(R[0,0]-R[1,1]-R[2,2]+1.0)
 if ( np.fabs(R[1,1]-R[2,2]-R[0,0]+1.0) < dEpsilon ):
  quat[2] = 0.0
 else:
  quat[2] = 0.5*np.sign(R[0,2]-R[2,0])*np.sqrt(R[1,1]-R[2,2]-R[0,0]+1.0)
 if ( np.fabs(R[2,2]-R[0,0]-R[1,1]+1.0) < dEpsilon ):
  quat[3] = 0.0
 else:
  quat[3] = 0.5*np.sign(R[1,0]-R[0,1])*np.sqrt(R[2,2]-R[0,0]-R[1,1]+1.0)

 return np.array(quat)

def TF2xyzquat(T):
 """
 Convert a homogeneous transformation matrix into the a vector containing the
 pose of the robot.

 Input:
  T -- A homogeneous transformation
 Output:
  X -- A pose vector in the format [x y z ew ex ey ez], donde la first part
       is Cartesian coordinates and the last part is a quaternion
 """
 quat = rot2quat(T[0:3,0:3])
 res = [T[0,3], T[1,3], T[2,3], quat[0], quat[1], quat[2], quat[3]]
 return np.array(res)


def jacobian(q, delta=0.0001):
    """
    Jacobiano analitico para la posicion. Retorna una matriz de 3x6 y toma como
    entrada el vector de configuracion articular q=[q1, q2, q3, q4, q5, q6]
    """
    # Crear una matriz 3x6
    J = np.zeros((3, 7))
    # Transformacion homogenea inicial (usando q)
    T = dhreal(q)


    # Iteracion para la derivada de cada columna
    for i in range(7):
        # Copiar la configuracion articular inicial
        dq = copy(q)
        T = dhreal(dq)
        # Incrementar la articulacion i-esima usando un delta
        dq[i] = dq[i] + delta
        # Transformacion homogenea luego del incremento (q+delta)
        dT = dhreal(dq)

        T_inc = dhreal(dq)
        # Aproximacion del Jacobiano de posicion usando diferencias finitas
        if (i==1 or i==6):
            J[0:3,i]=(T_inc[0:3, 3]-T[0:3, 3])*(0.01)/delta
        else:
            J[0:3,i]=(T_inc[0:3, 3]-T[0:3, 3])/delta
    return J


def ikine_es200(xdes, q0):
    """
    Calcular la cinematica inversa de ES200 numericamente a partir de la configuracion articular inicial de q0. 
    Emplear el metodo de newton
    """
    epsilon = 0.001
    max_iter = 1000
    delta    = 0.00001
    q = copy(q0)
    errors = []

    for i in range(max_iter):
        J = jacobian(q)
        f = dhreal(q)[0:3, 3]
        e = xdes - f
        errors.append(np.linalg.norm(e))
        q = q + np.dot(np.linalg.pinv(J), e)
        if np.linalg.norm(e) < epsilon:
            break

    return q, errors


